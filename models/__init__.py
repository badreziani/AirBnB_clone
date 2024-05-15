#!/usr/bin/python3
"""
__init__ module - create a unique FileStorage instance
                for our application.
"""


from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
