#!/usr/bin/python3
"""This module provides the definition of the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from the BaseModel class."""

    place_id = ''
    user_id = ''
    text = ''
