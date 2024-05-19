#!/usr/bin/python3
"""This module define a class"""

from datetime import datetime
import uuid
import models

class BaseModel:
    """This class defines a blueprint called BaseModel"""

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
            models.storage.new(self)

    def __str__(self):
        """Unofficial representation of instance"""

        class_name = self.__class__.__name__
        instance_id = self.id
        instance_dict = self.__dict__

        return "[{:s}] ({:s}) {}".format(
                class_name, instance_id, instance_dict
                )

    def save(self):
        """Updates time stamp on instance"""

        # isoformat added to make object serializable when dumped
        # cos it fails on datetime object not being serializable.
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of instance"""

        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__

        if not isinstance(self.created_at, str):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        if not isinstance(self.updated_at, str):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        # update created_at and updated_at values in dictionary
        instance_dict["created_at"] = created_at
        instance_dict["updated_at"] = updated_at

        return instance_dict
