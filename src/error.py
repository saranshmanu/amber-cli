class APIKeyNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "OpenAI API key is empty"
        super().__init__(self.message)


class APIKeyNotValidException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "OpenAI API key is not valid"
        super().__init__(self.message)


class PromptNotValidException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Prompt is either empty or not valid"
        super().__init__(self.message)


class ModelNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Model is not set"
        super().__init__(self.message)


class ModelNotValidException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Model is not supported"
        super().__init__(self.message)
