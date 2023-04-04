class APIKeyNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "OpenAI API key is empty"
        super().__init__(self.message)


class PromptNotSetException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = "Prompt is empty"
        super().__init__(self.message)
