#import
import os
import csv
import numpy as np
#Reading CSV file
election_csv= os.path.join("PyPoll/Resources/election_data.csv")
pypoll = []
with open (election_csv) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for data in csvreader:
        pypoll.append(data)
    # print(pypoll)

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

#Finding total number of votes
ballot_id =[]
for i in pypoll:
     ballot_id.append(str(i[0]))
     total_votes= len(ballot_id)
     
print(total_votes)



#created trackers for each candidate to track how many votes each of them recieved
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

#Calculated percentage of votes Diana recieved
diana_percent = [f"{round(Diana_DeGette/int(total_votes),5)*100}%", f"{Diana_DeGette}"]
print(diana_percent)

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

#Calculated percentage of votes Charles recieved
Charles_percent = [f"{round(Charles_Casper_Stockham/int(total_votes),5)*100}%", f"{Charles_Casper_Stockham}"]
print(Charles_percent)

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

#Calculated percentage of votes Raymon recieved
Raymon_percent = [f"{round(Raymon_Anthony_Doane/int(total_votes),4)*100}%", f"{Raymon_Anthony_Doane}"]
print(Raymon_percent)

#Finding who won based on popular vote
if Diana_DeGette > Charles_Casper_Stockham and Raymon_Anthony_Doane:
    winner = Diana
elif Charles_Casper_Stockham > Diana_DeGette and Raymon_Anthony_Doane:
    winner = Charles
else:
    winner = Raymon

Results= ["Election Results","-------------",
f"Total Votes: {total_votes}","----------",
f"{Charles}: {Charles_percent[0]}, ({Charles_percent[1]})" ,
f"{Diana}: {diana_percent[0]}, ({diana_percent[1]})  ",
f"{Raymon}: {Raymon_percent[0]}, ({Raymon_percent[1]})",
"------------",
f"Winner: {winner}",
"------------"]

with open ("PyPoll/Analysis/election_data.txt",'w') as a:
    for i in Results:
        a.write(i)
        a.write('\n')


for i in Results:
    print(i)