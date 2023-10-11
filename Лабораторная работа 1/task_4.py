users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_dict = {"Общее количество": 0, "Уникальные посещения": 0}
unique = set(users)
total = len(users)
total_unique = len(unique)
users_dict["Общее количество"] = total
users_dict["Уникальные посещения"] = total_unique

print(users_dict)

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
