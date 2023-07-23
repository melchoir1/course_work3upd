import json
from sorted_file import sorted_date


if __name__ == "__main__":
    with open('operations.json') as f:
        file_content = f.read()
        templates = json.loads(file_content)

    # Вызов функции sorted_date и передача данных из operations.json.
    last_operations = sorted_date(templates)
    for operation in last_operations:
        print("-" * 40)  # Разделитель
        print(operation)
