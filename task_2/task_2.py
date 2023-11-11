# TODO импортировать необходимые молули
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    res_list = []  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as fin:
        reader = csv.DictReader(fin, delimiter=',', quotechar='\n')
        for i in reader:
            res_list.append(i)

    with open(OUTPUT_FILENAME, 'w') as fout:  # TODO Сериализовать в файл с отступами равными 4
        json.dump(res_list, fout, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
