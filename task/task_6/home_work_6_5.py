# Прочитать сохраненный csv файл и сохранить данные в excel файл,
# кроме возроста - столбец с данными не нужен

import csv
import openpyxl

with open("test.csv") as csv_file:
    reader = csv.reader(csv_file)

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    for row_index, row in enumerate(reader):
        for column_index, value in enumerate(row):
            sheet.cell(row=row_index +1, column=column_index +1, value=value)
    workbook.save("test.xlsx")