# Day 13: LangChain Expression Language (LCEL) & Custom Tool Chains

## 💡 Concept Overview
LangChain Expression Language (LCEL) uses pipe operators (`prompt | llm | output_parser`) to compose modular, declarative, and async-ready LLM application chains.

## 🎯 Backend Scenario
Build custom Runnable chain components:
1. `PromptTemplate`: Formats string templates with input kwargs.
2. `StrOutputParser`: Strips whitespace and parses string responses.
3. `RunnableChain`: Implements `pipe(other)` operator overloading (`chain1 | chain2`) to execute combined Runnable pipelines.

## 🛠️ Instructions
1. Implement Runnable chain in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 13
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 13
   ```
