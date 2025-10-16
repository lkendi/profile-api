"""A FastAPI app that provides user profile
information and a random cat fact."""

from datetime import datetime, timezone
from fastapi import FastAPI, Request
import httpx
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from models import User
from typing import Any, cast

limiter = Limiter(key_func=get_remote_address)

app = FastAPI()

api_v1 = FastAPI()

app.mount("/v1", api_v1)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded,
                          cast(Any, _rate_limit_exceeded_handler))

user = User(
    name="Lucy Kendi",
    email="lkendi003@gmail.com",
    stack="Python/FastAPI",
)


@app.get("/me")
@limiter.limit("5/minute")
async def get_me(request: Request):

    """
    Returns information about the user as well as a random cat fact.

    The returned object contains the following fields:
    - status: a string indicating the status of the response.
    - user: a dictionary containing the user's email, name, and stack.
    - timestamp: a string representing the current timestamp
                (UTC - ISO 8601 format).
    - fact: a string containing a random cat fact.
    """
    cat_fact = await get_cat_fact()

    return {
        "status": "success",
        "user": {
            "email": user.email,
            "name": user.name,
            "stack": user.stack
        },
        "timestamp": datetime.now(timezone.utc)
        .isoformat().replace("+00:00", "Z"),
        "fact": cat_fact
    }


async def get_cat_fact():
    """
    Helper function that returns a random cat fact from the specified API.
    """
    url = "https://catfact.ninja/fact"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=5.0)
            response.raise_for_status()
            data = response.json()
            return data.get("fact", "No cat fact available at the moment.")
    except (httpx.RequestError, httpx.HTTPStatusError):
        return "No cat fact available at the moment. Please try again later."
