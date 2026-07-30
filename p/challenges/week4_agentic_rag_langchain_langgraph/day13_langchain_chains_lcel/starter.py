from typing import Any, Callable, Dict

class Runnable:
    def invoke(self, input_data: Any) -> Any:
        raise NotImplementedError

    def __or__(self, other: 'Runnable') -> 'RunnableChain':
        # TODO: Implement pipe operator | chaining
        pass

class RunnableChain(Runnable):
    def __init__(self, first: Runnable, second: Runnable):
        self.first = first
        self.second = second

    def invoke(self, input_data: Any) -> Any:
        # TODO: Sequential chain execution
        pass

class PromptTemplate(Runnable):
    def __init__(self, template: str):
        self.template = template

    def invoke(self, input_data: Dict[str, Any]) -> str:
        # TODO: Format template with input dict
        pass

class StrOutputParser(Runnable):
    def invoke(self, input_data: str) -> str:
        # TODO: Clean and return string
        pass
