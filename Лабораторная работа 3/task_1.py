# TODO Напишите функцию для поиска индекса товара
def index_finder(items, tovar):
    idx = -1
    counter = 1
    for i in range (len(items)):
        if tovar == items[i] and counter == 1:
            idx = i
            counter += 1
    if idx != -1:
        return idx
    else: return None



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_finder(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
