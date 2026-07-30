from typing import Dict, Any

class RAGEvaluator:
    def calculate_faithfulness(self, answer: str, context: str) -> float:
        """Measures what percentage of answer claims are present in context."""
        answer_tokens = set(t.lower().strip(".,!?:;") for t in answer.split() if len(t.strip(".,!?:;")) > 2)
        context_tokens = set(t.lower().strip(".,!?:;") for t in context.split() if len(t.strip(".,!?:;")) > 2)

        if not answer_tokens:
            return 1.0

        supported = answer_tokens.intersection(context_tokens)
        score = len(supported) / len(answer_tokens)
        return round(score, 4)

    def calculate_answer_relevance(self, question: str, answer: str) -> float:
        """Measures keyword overlap between question and generated answer."""
        question_tokens = set(q.lower().strip(".,!?:;") for q in question.split() if len(q.strip(".,!?:;")) > 2)
        answer_tokens = set(a.lower().strip(".,!?:;") for a in answer.split() if len(a.strip(".,!?:;")) > 2)

        if not question_tokens:
            return 1.0

        overlap = question_tokens.intersection(answer_tokens)
        score = len(overlap) / len(question_tokens)
        return round(score, 4)

    def evaluate(self, question: str, answer: str, context: str) -> Dict[str, float]:
        faithfulness = self.calculate_faithfulness(answer, context)
        relevance = self.calculate_answer_relevance(question, answer)
        harmonic_mean = (2 * faithfulness * relevance) / (faithfulness + relevance) if (faithfulness + relevance) > 0 else 0.0

        return {
            "faithfulness": faithfulness,
            "answer_relevance": relevance,
            "overall_score": round(harmonic_mean, 4)
        }
