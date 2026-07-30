import pytest
from challenges.week4_agentic_rag_langchain_langgraph.day14_langgraph_stateful_agents.solution import (
    StateGraph,
    END
)

def test_stategraph_direct_edges():
    graph = StateGraph()
    graph.add_node("step1", lambda state: {"count": state.get("count", 0) + 1})
    graph.add_node("step2", lambda state: {"count": state["count"] * 2})
    graph.add_edge("step1", "step2")
    graph.add_edge("step2", END)

    result = graph.invoke("step1", {"count": 5})
    assert result["count"] == 12

def test_stategraph_conditional_routing_loop():
    graph = StateGraph()
    graph.add_node("increment", lambda state: {"counter": state["counter"] + 1})

    def route_condition(state: dict) -> str:
        if state["counter"] < 3:
            return "increment"
        return END

    graph.add_conditional_edges("increment", route_condition)

    res = graph.invoke("increment", {"counter": 0})
    assert res["counter"] == 3
