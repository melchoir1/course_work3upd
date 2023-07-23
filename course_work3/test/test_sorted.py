import pytest
from datetime import datetime
from sorted_file import sorted_date

# данные для тестирования
TEMPLATES = [
    {
        "state": "EXECUTED",
        "description": "Transaction 1",
        "operationAmount": {"amount": 100, "currency": {"name": "USD"}},
        "date": "2023-07-23T10:00:00.000000",
        "from": "1234567890123456",
        "to": "9876543210987654"
    },
    {
        "state": "EXECUTED",
        "description": "Transaction 2",
        "operationAmount": {"amount": 200, "currency": {"name": "EUR"}},
        "date": "2023-07-22T15:30:00.000000",
        "from": "1111222233334444",
        "to": "5555666677778888"
    },
]

def test_sorted_date():
    formatted_operations = sorted_date(TEMPLATES)
    """ Проверяем, что результат является списком """
    assert isinstance(formatted_operations, list)

    """ Проверяем, что возвращается не более 5 операций """
    assert len(formatted_operations) <= 5

    """ Проверяем, что нет пустых строк в результате """
    assert all(operation.strip() for operation in formatted_operations)

