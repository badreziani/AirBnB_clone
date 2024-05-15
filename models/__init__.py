#!/usr/bin/python3
"""
__init__ module - create a unique FileStorage instance
                for our application.
"""



from .engine.file_storage import FileStorage
print("============= Before ============")
storage = FileStorage()
print("======== Storage created ========")
storage.reload()
print("======== Reload called ==========")
