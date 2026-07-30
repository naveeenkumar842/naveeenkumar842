# Day 14: LangGraph Stateful Agents & Graph Routing

## 💡 Concept Overview
LangGraph models agent workflows as stateful cyclic graphs with nodes (execution functions) and edges (transition paths), enabling loops, memory, human-in-the-loop, and multi-agent systems.

## 🎯 Backend Scenario
Build a graph runtime `StateGraph`:
1. `add_node(name: str, func: Callable[[dict], dict])`: Registers state modification node.
2. `add_edge(start: str, end: str)`: Connects two nodes.
3. `add_conditional_edges(start: str, condition_func: Callable[[dict], str])`: Dynamically routes graph execution based on current state.
4. `compile().invoke(initial_state: dict) -> dict`: Executes state transitions from `START` to `END`.

## 🛠️ Instructions
1. Implement in `starter.py`.
2. Test your solution:
   ```bash
   python daily_push.py --test 14
   ```
3. Complete and push:
   ```bash
   python daily_push.py --complete 14
   ```
