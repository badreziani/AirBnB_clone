#!/usr/bin/python3
"""New Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
