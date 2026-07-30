from typing import Dict, Any, Callable

END = "__END__"

class StateGraph:
    def __init__(self):
        self.nodes: Dict[str, Callable[[Dict[str, Any]], Dict[str, Any]]] = {}
        self.edges: Dict[str, str] = {}
        self.conditional_edges: Dict[str, Callable[[Dict[str, Any]], str]] = {}

    def add_node(self, name: str, func: Callable[[Dict[str, Any]], Dict[str, Any]]) -> None:
        self.nodes[name] = func

    def add_edge(self, start: str, end: str) -> None:
        self.edges[start] = end

    def add_conditional_edges(
        self,
        start: str,
        condition_func: Callable[[Dict[str, Any]], str]
    ) -> None:
        self.conditional_edges[start] = condition_func

    def invoke(self, start_node: str, initial_state: Dict[str, Any], max_steps: int = 20) -> Dict[str, Any]:
        current_node = start_node
        state = dict(initial_state)
        steps = 0

        while current_node != END and steps < max_steps:
            if current_node not in self.nodes:
                raise ValueError(f"Node '{current_node}' not defined in graph")

            node_func = self.nodes[current_node]
            state_update = node_func(state)
            state.update(state_update)
            steps += 1

            if current_node in self.conditional_edges:
                cond_func = self.conditional_edges[current_node]
                current_node = cond_func(state)
            elif current_node in self.edges:
                current_node = self.edges[current_node]
            else:
                break

        return state
