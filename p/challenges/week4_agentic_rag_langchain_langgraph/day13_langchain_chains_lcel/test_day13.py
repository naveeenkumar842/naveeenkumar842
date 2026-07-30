import pytest
from challenges.week4_agentic_rag_langchain_langgraph.day13_langchain_chains_lcel.solution import (
    PromptTemplate,
    MockLLM,
    StrOutputParser
)

def test_lcel_pipe_chain_execution():
    prompt = PromptTemplate("Summarize the topic: {topic}")
    llm = MockLLM(lambda p: f"  Summary of {p.split(': ')[-1]}  ")
    parser = StrOutputParser()

    chain = prompt | llm | parser

    result = chain.invoke({"topic": "FastAPI Async Operations"})
    assert result == "Summary of FastAPI Async Operations"
