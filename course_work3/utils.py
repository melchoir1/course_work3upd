import datetime


def filter_sort(templates):
    items_list = [item for item in templates if item.get("state") == "EXECUTED"]
    items_list.sort(key=lambda x: x.get("date"), reverse=True) # todo почитать про key=lamda
    return items_list


def prepare_message(items_list):
    result = [] # todo делаем пустой список с целью пройтись по нему и вытащить необходимые значения
    for item in items_list:
        description = item.get("description")
        amount = item.get("operationAmount").get("amount")
        currency = item.get("operationAmount").get("currency").get("name")
        date = item.get("date")
        date_format = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')  # todo приводим в строку
        """понимаю что надо было сделать отдельную функцию с operations, transit
           но я получил данные и потом понял что забыл поставить звездочки и пришлось колхозить 
           и поэтому функция выглядит не очень"""
        operations = item.get("from")
        operations_data = f"{operations[:-12]} {operations[-12:-10]}{'*' * 2} {'*' * 4} {operations[-4:]}" if operations is not None else ""
        transit = item.get("to")
        transit_data = transit[0:4] + " " + "*" * 2 + transit[-4:]
        result.append((date_format, description, amount, currency, operations_data, transit_data))
    return result


