"""User model definition."""

from pydantic import BaseModel


class User(BaseModel):
    """
    A model representing a user with their name, email, and tech stack.
    """
    name: str
    email: str
    stack: str
