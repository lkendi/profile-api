"""
Tests for `main.py`.
"""

from unittest.mock import patch
import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio
async def test_get_me_success():
    """
    Test the /me endpoint on a successful run
    by mocking the external API then checking the
    correctness of structure and data returned.
    """
    with patch("main.get_cat_fact",
               return_value="A mock cat fact.") as mock_get_fact:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport,
                               base_url="http://test") as client:
            response = await client.get("/me")

        mock_get_fact.assert_called_once()
        assert response.status_code == 200

        data = response.json()

        assert data["status"] == "success"
        assert data["user"]["name"] == "Lucy Kendi"
        assert data["user"]["email"] == "lkendi003@gmail.com"
        assert data["user"]["stack"] == "Python/FastAPI"
        assert data["timestamp"].endswith("Z")
        assert data["fact"] == "A mock cat fact."


@pytest.mark.asyncio
async def test_get_me_cat_fact_api_failure():
    """
    Test the /me endpoint when the external API fails.
    The endpoint should still return a 200 OK with a fallback message.
    """
    fallback_message = "Could not retrieve a cat fact at this time."

    with patch("main.get_cat_fact",
               return_value=fallback_message) as mock_get_fact:
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport,
                               base_url="http://test") as client:
            response = await client.get("/me")

        mock_get_fact.assert_called_once()
        assert response.status_code == 200

        data = response.json()

        assert data["status"] == "success"
        assert data["user"]["name"] == "Lucy Kendi"
        assert data["fact"] == fallback_message
