from .application_error import ApplicationError

COURSE_NOT_FOUND = "COURSE_NOT_FOUND", "Course not found."
ERROR_CREATING_MODULE = "ERROR_CREATING_MODULE", "Could not create module."

__all__ = ["ApplicationError", "COURSE_NOT_FOUND"]
