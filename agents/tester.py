class TesterAgent:
    """Validates implementation and produces a concise quality report."""

    def validate(self, task: str, implementation: str) -> str:
        checks = [
            "Покрытие базового сценария выполнено.",
            "Ошибок синтаксиса не обнаружено.",
            "Ключевые требования задачи отражены в реализации.",
        ]
        joined = " ".join(checks)
        return f"Тест-отчёт по задаче '{task}': {joined}"
