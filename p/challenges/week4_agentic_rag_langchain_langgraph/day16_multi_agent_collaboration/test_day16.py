import pytest
from challenges.week4_agentic_rag_langchain_langgraph.day16_multi_agent_collaboration.solution import MultiAgentSupervisor

def test_multi_agent_supervisor_routing():
    supervisor = MultiAgentSupervisor()
    supervisor.register_agent("researcher", lambda q: "Found paper on Async Python")
    supervisor.register_agent("coder", lambda q: "def async_func(): pass")

    res = supervisor.execute_workflow("Research and code Python async function")
    assert "researcher" in res["delegated_agents"]
    assert "coder" in res["delegated_agents"]
    assert "[researcher]" in res["final_synthesis"]
    assert "[coder]" in res["final_synthesis"]

def test_multi_agent_supervisor_single_agent():
    supervisor = MultiAgentSupervisor()
    supervisor.register_agent("researcher", lambda q: "Research findings")
    supervisor.register_agent("coder", lambda q: "Code output")

    res = supervisor.execute_workflow("Search for latest LLM papers")
    assert res["delegated_agents"] == ["researcher"]
