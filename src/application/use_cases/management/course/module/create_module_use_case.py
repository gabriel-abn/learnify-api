from src.application.common import (
    COURSE_NOT_FOUND,
    ERROR_CREATING_MODULE,
    ApplicationError,
)
from src.application.repositories import ICourseRepository, IModuleRepository
from src.domain.use_cases.management.course.module.create_module import (
    CreateModule,
    CreateModuleParams,
    CreateModuleResult,
)


class CreateModuleUseCase(CreateModule):
    def __init__(
        self, course_repository: ICourseRepository, module_repository: IModuleRepository
    ):
        self.course_repository = course_repository
        self.module_repository = module_repository

    def execute(self, params: CreateModuleParams) -> CreateModuleResult:
        course_id = params["course_id"]

        course_exists, course = self.course_repository.get(course_id)

        if not course_exists:
            raise ApplicationError(COURSE_NOT_FOUND)

        course.init_modules()
        course.add_module(title=params["title"])

        module = course.get_module(course.modules[-1].module_id)

        created, module_id = self.module_repository.create(module)

        if not created:
            raise ApplicationError(ERROR_CREATING_MODULE)

        return {
            "module_id": module_id,
            "course_id": course_id,
            "position": module.position,
        }
