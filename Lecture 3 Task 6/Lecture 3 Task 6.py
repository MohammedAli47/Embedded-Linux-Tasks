import os
import openpyxl


directory = os.path.dirname(os.path.abspath(__file__))
workbook = openpyxl.load_workbook(directory + "\\database.xlsx")
sheet = workbook.active

workbook.save(directory + "\\database.xlsx")
