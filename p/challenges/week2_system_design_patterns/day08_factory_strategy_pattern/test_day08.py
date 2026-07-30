import pytest
from challenges.week2_system_design_patterns.day08_factory_strategy_pattern.solution import (
    PaymentProcessorFactory,
    StripePaymentStrategy,
    PayPalPaymentStrategy
)

def test_factory_creates_stripe_strategy():
    processor = PaymentProcessorFactory.create_processor("stripe")
    assert isinstance(processor, StripePaymentStrategy)
    res = processor.process_payment(99.99, "usd")
    assert res["provider"] == "STRIPE"
    assert res["status"] == "SUCCESS"
    assert "ch_stripe_" in res["transaction_id"]

def test_factory_creates_paypal_strategy():
    processor = PaymentProcessorFactory.create_processor("PayPal")
    assert isinstance(processor, PayPalPaymentStrategy)
    res = processor.process_payment(49.00, "eur")
    assert res["provider"] == "PAYPAL"
    assert res["status"] == "SUCCESS"

def test_factory_unsupported_provider_raises():
    with pytest.raises(ValueError) as exc_info:
        PaymentProcessorFactory.create_processor("crypto_pay")
    assert "Unsupported payment provider" in str(exc_info.value)
