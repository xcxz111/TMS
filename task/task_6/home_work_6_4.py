# Прочитать сохраненный json-файл и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец "телефон".

import json
import csv

with open("test.json") as file:
    test = json.load(file)

test["phone"] = "value"

with open("test.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["111111", "222222", "333333", "444444", "555555", "phone"])
    writer.writeheader()
    writer.writerow(test)

