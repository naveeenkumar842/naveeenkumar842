import pytest
from challenges.week5_mlops_eval_production.day19_quantization_onnx_serving.solution import ProductionInferenceEngine

def test_inference_engine_predict_single():
    engine = ProductionInferenceEngine()
    res = engine.predict_single([1.0, 2.0])
    assert res == [2.5, 4.5]

def test_inference_engine_dynamic_batching():
    engine = ProductionInferenceEngine()
    requests = [[1.0], [2.0], [3.0], [4.0], [5.0]]
    results = engine.enqueue_and_process(requests, max_batch_size=2)

    assert len(results) == 5
    assert results[0] == [2.5]
    assert results[4] == [10.5]
