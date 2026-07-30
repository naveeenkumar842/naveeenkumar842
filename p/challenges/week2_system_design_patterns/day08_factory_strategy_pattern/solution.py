from abc import ABC, abstractmethod
from typing import Dict, Any

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        pass

class StripePaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        return {
            "status": "SUCCESS",
            "provider": "STRIPE",
            "amount": amount,
            "currency": currency.upper(),
            "transaction_id": f"ch_stripe_{int(amount * 100)}"
        }

class PayPalPaymentStrategy(PaymentStrategy):
    def process_payment(self, amount: float, currency: str) -> Dict[str, Any]:
        return {
            "status": "SUCCESS",
            "provider": "PAYPAL",
            "amount": amount,
            "currency": currency.upper(),
            "transaction_id": f"PAYID-PAYPAL-{int(amount * 100)}"
        }

class PaymentProcessorFactory:
    _STRATEGIES = {
        "stripe": StripePaymentStrategy,
        "paypal": PayPalPaymentStrategy
    }

    @classmethod
    def create_processor(cls, provider: str) -> PaymentStrategy:
        provider_key = provider.lower().strip()
        if provider_key not in cls._STRATEGIES:
            raise ValueError(f"Unsupported payment provider: {provider}")
        return cls._STRATEGIES[provider_key]()
