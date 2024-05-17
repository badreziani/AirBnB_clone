#/bin/usr/python3
"""
user module - contains definition for class User
"""

from .base_model import BaseModel


class User(BaseModel):
    """Class User
    Public class attributes:
        email: string
        password: string
        first_name: string
        last_name: string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
