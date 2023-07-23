import datetime
from utils import filter_sort, prepare_message

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
        "state": "PENDING",
        "description": "Transaction 2",
        "operationAmount": {"amount": 50, "currency": {"name": "EUR"}},
        "date": "2023-07-22T15:30:00.000000",
        "from": "1111222233334444",
        "to": "5555666677778888"
    },
]

def test_filter_sort():
    result = filter_sort(TEMPLATES)
    """ Проверяем, что результат является списком """
    assert isinstance(result, list)

    """ Проверяем, что результат отсортирован по дате в обратном порядке """
    dates = [item.get("date") for item in result]
    assert dates == sorted(dates, reverse=True)

    """ Проверяем, что в результате есть только элементы с "state" равным "EXECUTED """
    states = [item.get("state") for item in result]
    assert all(state == "EXECUTED" for state in states)
