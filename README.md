### Python-Challenge

## General Information
In this challenge I used Python to analyze two different data sets. I started with PyBank where I analyzed financial records for a company and made an analysis to find that companies total number of months, net profit/losses, the average change in profits/losses, greates increase in profits, and greatest decrease in profits. Then I worked on Pypoll where I analyzed election data and created an analysis to find total number of votes, complete list of candidates, the total number of votes and percentage of votes each candidate recieved, and the winner based off popular vote.

## Technologies Used
* Python
* VS Code

## Process - PyBank
1. I started PyBank by loading the CSV file 
2. Defined my variables for finding total number of months and total profit 
3. Wrote code to find both months and profit
```
months = []
for i in pybank:
    months.append(str(i[0]))
# print(months)
months_counter = len(months)
# print(months_counter)
```
```
profits = []
for i in pybank:
    profits.append(int(i[1]))
# print(profits)
total_profits = sum(profits)
# print(total_profits)
```
4. Calculated total change in profits/losses over the entire period of time
5. Found the average of the changes
```
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
```
6. Wrote code to find the months with the greatest increase and decrease of profits
7. Wrote code to ouput my analysis

## Process - PyPoll
1. I started PyPoll by loading the CSV file 
2. Defined my variables and created arrays to organize my work
3. Wrote code to find all the candidates names
```
#Finding all candidates names and assigning them to variables.
all_candidates = []
for i in pypoll:
    all_candidates.append(str(i[2]))

list(all_candidates)

def unique(all_candidates):
    candidate_name = np.array(all_candidates)
candidate_name = np.unique(all_candidates)
print(candidate_name)
Charles = candidate_name[0]
Diana = candidate_name[1]
Raymon = candidate_name[2]
```
4. Wrote code to find total number of votes
5. Created a counter for each candidate to loop through the CSV and count how many votes each candidate recieved.
```
#Diana Tracker
def countX(all_candidates, x):
    count = 0
    for i in all_candidates:
        if (i == x):
            count = count + 1
    return count
x = "Diana DeGette"
print("{} has occured {} times".format(x, countX(all_candidates,x)))
Diana_DeGette = 272892

#Charles tracker
def countX(all_candidates, x):
    count = 0
    for i in all_candidates:
        if (i == x):
            count = count + 1
    return count
x = "Charles Casper Stockham"
print("{} has occured {} times".format(x, countX(all_candidates,x)))
Charles_Casper_Stockham = 85213

#Raymon tracker
def countX(all_candidates, x):
    count = 0
    for i in all_candidates:
        if (i == x):
             count = count + 1
    return count
x = "Raymon Anthony Doane"
print("{} has occured {} times".format(x, countX(all_candidates,x)))
Raymon_Anthony_Doane = 11606
```
6. Wrote code to find the percentage of how many votes each candidate recieved
```
#Calculated percentage of votes Diana recieved
diana_percent = [f"{round(Diana_DeGette/int(total_votes),5)*100}%", f"{Diana_DeGette}"]
print(diana_percent)

#Calculated percentage of votes Charles recieved
Charles_percent = [f"{round(Charles_Casper_Stockham/int(total_votes),5)*100}%", f"{Charles_Casper_Stockham}"]
print(Charles_percent)

#Calculated percentage of votes Raymon recieved
Raymon_percent = [f"{round(Raymon_Anthony_Doane/int(total_votes),4)*100}%", f"{Raymon_Anthony_Doane}"]
print(Raymon_percent)
```
7. Wrote code to find the winner of the election by popular vote
8. wrote code to output my analysis

