# Day 19: High-Throughput Production Inference & Batching Engine

## 💡 Concept Overview
In production MLOps, serving ML models one request at a time wastes GPU/CPU SIMD parallelism. Dynamic batching collects concurrent requests within a small time window (e.g. 5ms) and executes batch matrix inference in a single vector operation.

## 🎯 Backend Scenario
Build `ProductionInferenceEngine`:
1. `predict_single(input_vector: List[float]) -> List[float]`: Single request prediction interface.
2. `predict_batch(batch_vectors: List[List[float]]) -> List[List[float]]`: Optimized batch matrix inference engine.
3. `enqueue_and_process(requests: List[List[float]], max_batch_size: int = 4) -> List[List[float]]`: Chunks requests into dynamic batches and executes inference.

## 🛠️ Instructions
1. Implement in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 19
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 19
   ```
