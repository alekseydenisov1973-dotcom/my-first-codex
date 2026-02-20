from orchestrator import Orchestrator


def main() -> None:
    task = "Создать прототип многоагентной разработки"
    orchestrator = Orchestrator()
    result = orchestrator.run(task)

    print("=== Результат оркестрации ===")
    print(f"Задача: {result['task']}")
    print("\n--- Архитектура ---")
    print(result["architecture"])
    print("\n--- Реализация ---")
    print(result["implementation"])
    print("\n--- Тестирование ---")
    print(result["test_report"])
    print("\n--- История ---")
    for record in result["history"]:
        print(f"- {record}")


if __name__ == "__main__":
    main()
