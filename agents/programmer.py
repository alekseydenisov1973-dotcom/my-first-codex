class ProgrammerAgent:
    """Produces implementation plan or draft code based on architecture."""

    def implement(self, task: str, architecture: str) -> str:
        return (
            f"Для задачи '{task}' подготовлен каркас реализации.\n"
            "Использована архитектура:\n"
            f"{architecture}\n"
            "Результат: создана структура модулей и базовые сценарии обработки."
        )
