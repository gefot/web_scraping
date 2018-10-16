import random
from xlsxwriter import Workbook

workbook = Workbook('first_file.xlsx')

print("Starting")

worksheet = workbook.add_worksheet()

for row in range(20):
    a = random.randint(1, 20)
    worksheet.write(row, 0, 'Element')
    worksheet.write(row, 1, a)



workbook.close()