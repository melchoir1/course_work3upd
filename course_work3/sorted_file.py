from utils import filter_sort, prepare_message
from datetime import datetime


def sorted_date(templates):
    all_operations = filter_sort(templates)
    price_operations = prepare_message(all_operations)
    sorted_operations = sorted(price_operations, key=lambda x: datetime.strptime(x[0], '%d.%m.%Y'))
    last_operation = sorted_operations[-5:]
    # Форматирование операций в желаемом формате.
    formated_operations = []
    for operation in last_operation:
        date, description, amount, currency, sender, recipient = operation
        formatted_amount = '{:,.2f}'.format(float(amount)).replace(',', ' ')
        formated_operations.append(f"\n{date} {description}\n{sender} -> {recipient}\n{formatted_amount} {currency}\n")

    return formated_operations

