class ApplicationError(Exception):
    def __init__(self, error: tuple[str, str]) -> None:
        self.name = error[0]
        self.message = error[1]
        super().__init__(self.message)
