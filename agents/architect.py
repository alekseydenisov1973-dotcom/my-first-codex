class ArchitectAgent:
    """Designs high-level solution architecture for a given task."""

    def design(self, task: str) -> str:
        return (
            "1) Разделить систему на модули: интерфейс, бизнес-логика, данные.\n"
            "2) Определить контракт взаимодействия модулей.\n"
            "3) Выделить точки расширения и тестирования.\n"
            f"4) Учесть цель задачи: {task}."
        )
