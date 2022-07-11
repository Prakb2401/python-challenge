import os
import csv


csvfile=os.join.path.join("resources","budget_data.csv")
row_count = 0
rows = []
with open (r".\Resources\budget_data.csv") as csvfile: #Open and read CSV
    budgetCSV = csv.reader(csvfile, delimiter=",")
    next(budgetCSV)
    for row in budgetCSV:
            row_count = row_count+1
            rows.append(row)