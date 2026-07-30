import pytest
from challenges.week5_mlops_eval_production.day17_rag_evaluation_ragas.solution import RAGEvaluator

def test_rag_evaluator_high_faithfulness():
    evaluator = RAGEvaluator()
    question = "What framework is FastAPI built on?"
    context = "FastAPI is built on Starlette and Pydantic for high performance."
    answer = "FastAPI is built on Starlette and Pydantic."

    metrics = evaluator.evaluate(question, answer, context)
    assert metrics["faithfulness"] >= 0.8
    assert metrics["answer_relevance"] >= 0.5
    assert metrics["overall_score"] > 0.6

def test_rag_evaluator_hallucinated_answer():
    evaluator = RAGEvaluator()
    question = "What is the capital of France?"
    context = "Paris is the capital of France."
    answer = "Tokyo is a city in Japan."

    metrics = evaluator.evaluate(question, answer, context)
    assert metrics["faithfulness"] < 0.5
    assert metrics["answer_relevance"] < 0.5
