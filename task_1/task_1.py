# TODO решите задачу
import json
INPUT_FILE = "input.json"

def task() -> float:
    summa = 0.0
    with open(INPUT_FILE, 'r') as fin:
        value = json.load(fin)
    for i in value:
        summa += i["score"] * i["weight"]
    return round(summa, 3)

print(task())
