# Day 08: Factory & Strategy Design Patterns (Payment Processors)

## 💡 Concept Overview
The Strategy Pattern defines a family of interchangeable algorithms (e.g. Payment Providers: Stripe, PayPal, Crypto). The Factory Pattern encapsulates object creation without exposing creation logic to clients. Combining both yields decoupled, testable, and extensible backend code.

## 🎯 Backend Scenario
Design a multi-provider payment engine:
1. `PaymentStrategy` (Abstract Base Class / Interface): defines `process_payment(amount: float, currency: str) -> Dict[str, Any]`.
2. Implement strategies: `StripePaymentStrategy` and `PayPalPaymentStrategy`.
3. `PaymentProcessorFactory`: `create_processor(provider_name: str) -> PaymentStrategy`.

## 🛠️ Instructions
1. Implement classes in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 8
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 8
   ```
