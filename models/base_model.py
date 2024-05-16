#!/usr/bin/python3
"""
base_model module, contains the definition of
the BaseModel class.
"""

from datetime import datetime
import uuid

import models


class BaseModel:
    """
    BaseModel class

    Attributes:
        id: represents a unique identifier for the instanciated object.
            It's autogenerated using the uuid4() from uuid module
        """
    def __init__(self, *args, **kwargs):
        """Initialization method"""

        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)

                # set attributes of instance with dict keys/values parsed
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        # Add this object to __objects of storage instance
        models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object.
        """

        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """Updates the public instance attribute `updated_at`
        with the current datetime.
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """

        return dict({
            **self.__dict__,
            "__class__": self.__class__.__name__,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
            })
