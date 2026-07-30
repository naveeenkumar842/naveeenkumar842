from typing import Any, Callable, Dict

class Runnable:
    def invoke(self, input_data: Any) -> Any:
        raise NotImplementedError

    def __or__(self, other: 'Runnable') -> 'RunnableChain':
        return RunnableChain(self, other)

class RunnableChain(Runnable):
    def __init__(self, first: Runnable, second: Runnable):
        self.first = first
        self.second = second

    def invoke(self, input_data: Any) -> Any:
        first_result = self.first.invoke(input_data)
        return self.second.invoke(first_result)

class PromptTemplate(Runnable):
    def __init__(self, template: str):
        self.template = template

    def invoke(self, input_data: Dict[str, Any]) -> str:
        return self.template.format(**input_data)

class MockLLM(Runnable):
    def __init__(self, response_func: Callable[[str], str]):
        self.response_func = response_func

    def invoke(self, input_data: str) -> str:
        return self.response_func(input_data)

class StrOutputParser(Runnable):
    def invoke(self, input_data: str) -> str:
        return str(input_data).strip()
