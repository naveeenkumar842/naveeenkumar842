from typing import Dict, Any, Callable, List

class MultiAgentSupervisor:
    def __init__(self):
        self.agents: Dict[str, Callable[[str], str]] = {}

    def register_agent(self, name: str, agent_func: Callable[[str], str]) -> None:
        self.agents[name] = agent_func

    def route_task(self, task: str) -> List[str]:
        task_lower = task.lower()
        selected = []

        if "research" in task_lower or "find" in task_lower or "search" in task_lower:
            if "researcher" in self.agents:
                selected.append("researcher")

        if "code" in task_lower or "implement" in task_lower or "python" in task_lower:
            if "coder" in self.agents:
                selected.append("coder")

        if not selected:
            # Fallback to all agents if general task
            selected = list(self.agents.keys())

        return selected

    def execute_workflow(self, request: str) -> Dict[str, Any]:
        target_agents = self.route_task(request)
        agent_outputs = {}

        for agent_name in target_agents:
            agent_func = self.agents[agent_name]
            output = agent_func(request)
            agent_outputs[agent_name] = output

        # Synthesize supervisor summary
        synthesized = " | ".join(f"[{name}]: {out}" for name, out in agent_outputs.items())

        return {
            "request": request,
            "delegated_agents": target_agents,
            "outputs": agent_outputs,
            "final_synthesis": synthesized
        }
