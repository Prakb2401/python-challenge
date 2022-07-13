import os
import csv


#Reading CSV file
budget_csv= os.path.join("PyBank/Resources/budget_data.csv")
pybank = []
with open (budget_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for bank in csvreader:
        pybank.append(bank)

# print(pybank)

#Finding how many total months in csv file
months = []
for i in pybank:
    months.append(str(i[0]))
# print(months)
months_counter = len(months)
# print(months_counter)

#Finding total profits in csv file
profits = []
for i in pybank:
    profits.append(int(i[1]))
# print(profits)
total_profits = sum(profits)
# print(total_profits)

#Finding The changes in "Profit/Losses" over the entire period, and then the average of those changes
summay_table_row = 0
profit_change = 0
profit_losses = []
for summary_table_row in pybank:
    profit_change = profit_change +int(summary_table_row[1])
    # print(profit_change)

bottom_row = profits[0]

for summary_table_row in profits:
    change = int(summary_table_row) - int(bottom_row)
    profit_losses.append(change)
    bottom_row = summary_table_row
 # print(profit_losses)

total_change = sum(profit_losses)
average_change = round(total_change/months_counter,2)
# print(average_change)

current_row = 0
increase_prof = 0
for summary_table_row in profits:
    bottom_row = summary_table_row
if current_row > increase_prof:
        increase_prof = current_row


#Finding greatest increase in profits and date
greatest_months = list(zip(months, profit_losses))

increase_prof = max(profit_losses)
for i in greatest_months:
    if i[1] == increase_prof:
        greatest_month = i[0]
# print(greatest_month)
greatest_month_increase = [{greatest_month},{increase_prof}]


#Finding greates decrease in profits and date
decrease_prof = 0
decrease_prof = min(profit_losses)
for i in greatest_months:
    if i[1] == decrease_prof:
        least_month = i[0]
#print(least_month)
output = ["Financial Analysis",
"-----------------------",
f"Total Months: {months_counter}",
f"Total: ${total_profits}",
f"Average Change: ${average_change}",
f"Greatest Increase in Profits: {greatest_month}, ${increase_prof}",
f"Greatest Decrease in Profits: {least_month}, ${decrease_prof}"]

for i in output:
    print(i)

with open ("PyBank/Resources/budget_data.txt",'w') as a:
    for i in output:
        a.write(i)
        a.write('\n')