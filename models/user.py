#!/usr/bin/python3
"""This module provides the definition of the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from the BaseModel class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
