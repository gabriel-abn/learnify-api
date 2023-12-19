from src.application.common import ERROR_CREATE_COURSE
from src.application.common.application_error import ApplicationError
from src.application.repositories.course_repository import ICourseRepository
from src.domain.common.entity import UniqueEntityID
from src.domain.entities.course import Course
from src.domain.use_cases.management.course.create_course import (
    CreateCourse,
    CreateCourseParams,
    CreateCourseResult,
)


class CreateCourseUseCase(CreateCourse):
    def __init__(self, course_repository: ICourseRepository):
        self.course_repository = course_repository

    def execute(self, params: CreateCourseParams) -> CreateCourseResult:
        course = Course(
            {
                "name": params["name"],
                "description": params["description"],
                "category": params["category"],
                "price": params["price"],
                "course_id": UniqueEntityID.generate(),
                "instructor_id": "NOT_DEFINED",
            }
        )

        course_saved, course_id = self.course_repository.save(course)

        if course_saved:
            return {
                "id": course_id,
            }

        raise ApplicationError(ERROR_CREATE_COURSE)
