from .application_error import ApplicationError

ERROR_CREATE_COURSE = "ERROR_CREATE_COURSE", "Could not create course."
COURSE_NOT_FOUND = "COURSE_NOT_FOUND", "Course not found."

ERROR_CREATING_MODULE = "ERROR_CREATING_MODULE", "Could not create module."

__all__ = ["ApplicationError", "COURSE_NOT_FOUND"]
