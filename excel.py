import random
from xlsxwriter import Workbook
import xlrd

# Declarations
filename = 'first_file.xlsx'

# Write values to Excel workbook
try:

    workbook = Workbook(filename)

    print("Starting write")
    worksheet = workbook.add_worksheet()

    for row in range(20):
        a = random.randint(1, 20)
        worksheet.write(row, 0, 'Element')
        worksheet.write(row, 1, a)

    workbook.close()
    print("Ending write")

except Exception as ex:
    print(ex)


# Read values from Excel workbook
try:
    workbook = xlrd.open_workbook(filename)
    worksheet = workbook.sheet_by_index(0)

    rows = worksheet.nrows
    for row in range(rows):
        first_col, second_col = worksheet.row_values(row)
        if first_col != '':
            print(first_col, '   ', second_col)

except Exception as ex:
    print(ex)
