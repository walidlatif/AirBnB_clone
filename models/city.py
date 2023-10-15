"""This module provides the definition of the City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from the BaseModel class"""

    state_id = ''
    name = ''
