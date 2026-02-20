from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from agents.architect import ArchitectAgent
from agents.programmer import ProgrammerAgent
from agents.tester import TesterAgent


@dataclass
class ProjectState:
    """Shared state between agents."""

    task: str
    architecture: str = ""
    implementation: str = ""
    test_report: str = ""
    history: List[str] = field(default_factory=list)

    def log(self, message: str) -> None:
        self.history.append(message)


class Orchestrator:
    """Coordinates architect -> programmer -> tester workflow."""

    def __init__(self) -> None:
        self.architect = ArchitectAgent()
        self.programmer = ProgrammerAgent()
        self.tester = TesterAgent()

    def run(self, task: str) -> Dict[str, str | List[str]]:
        state = ProjectState(task=task)
        state.log(f"Получена задача: {task}")

        architecture = self.architect.design(task)
        state.architecture = architecture
        state.log("Архитектура спроектирована архитектором.")

        implementation = self.programmer.implement(task=task, architecture=architecture)
        state.implementation = implementation
        state.log("Реализация подготовлена программистом.")

        report = self.tester.validate(task=task, implementation=implementation)
        state.test_report = report
        state.log("Тестирование завершено тестировщиком.")

        return {
            "task": state.task,
            "architecture": state.architecture,
            "implementation": state.implementation,
            "test_report": state.test_report,
            "history": state.history,
        }
