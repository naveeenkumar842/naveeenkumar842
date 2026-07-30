from typing import List

class ProductionInferenceEngine:
    def predict_single(self, input_vector: List[float]) -> List[float]:
        """Applies linear projection activation output."""
        return [round(x * 2.0 + 0.5, 4) for x in input_vector]

    def predict_batch(self, batch_vectors: List[List[float]]) -> List[List[float]]:
        """Executes batch vector prediction."""
        return [self.predict_single(vec) for vec in batch_vectors]

    def enqueue_and_process(
        self,
        requests: List[List[float]],
        max_batch_size: int = 4
    ) -> List[List[float]]:
        """Splits incoming requests into optimal dynamic batches."""
        all_results = []
        for i in range(0, len(requests), max_batch_size):
            batch = requests[i:i + max_batch_size]
            batch_predictions = self.predict_batch(batch)
            all_results.extend(batch_predictions)

        return all_results
