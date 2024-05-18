#!/usr/bin/python3
"""New City Class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class that inherits from BaseModel"""

    state_id = ""
    name = ""
