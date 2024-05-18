#!/usr/bin/python3
"""New User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """User Class that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
