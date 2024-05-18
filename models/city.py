#/bin/usr/python3
"""
city module - contains definition for class City
"""

from .base_model import BaseModel


class City(BaseModel):
    """Class City
    Public class attributes:
        state_id: string, represents State.id
        name: string
    """

    state_id = ""
    name = ""
