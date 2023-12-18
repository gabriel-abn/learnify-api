from src.application.common import ApplicationError
from src.application.repositories import ICourseRepository, ILessonRepository
from src.domain.common.entity import UniqueEntityID
from src.domain.use_cases.management.course.lesson.create_lesson import (
    CreateLesson,
    CreateLessonParams,
    CreateLessonResult,
)

COURSE_NOT_FOUND = "COURSE_NOT_FOUND", "Course not found."


class CreateLessonUseCase(CreateLesson):
    def __init__(
        self,
        lesson_repository: ILessonRepository,
        course_repository: ICourseRepository,
    ) -> None:
        self.lesson_repository = lesson_repository
        self.course_repository = course_repository

    def execute(self, params: CreateLessonParams) -> CreateLessonResult:
        course = self.course_repository.get(params["course_id"])

        if not course[0]:
            raise ApplicationError(COURSE_NOT_FOUND)

        lesson_id = UniqueEntityID.generate()

        course[1].add_lesson(
            module_id=params["module_id"],
            lesson_id=lesson_id,
            title=params["title"],
            description=params["description"],
            content_type=params["content_type"] if params["content_type"] else "video",
            content_url=params["content_url"] if params["content_url"] else ["any_url"],
        )

        lesson = course[1].get_lesson(
            module_id=params["module_id"], lesson_id=lesson_id
        )

        self.lesson_repository.save(lesson)

        return {"lesson_id": lesson_id}
