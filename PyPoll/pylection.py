# Unit 3 HW election poll
import os
import csv

# Variable list
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# data source location
csvpath = os.path.join('UCBSF201908DATA2' , '01-Lesson-Plans' , '03-Python' , 'Homework' , 'PyPoll' , 'Resources' , 'election_data.csv')


with open(csvpath, newline='') as csvfile:

    # list the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')


    csv_header = next(csvfile)

    for row in csvreader:

        # calculating votes
        total_votes += 1

        # Candidates lists
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

    # Calculating candidate percentages (divide by total votes?)
    kahn_percent = khan_votes / total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    # running if statements for winners
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley"

# printout
print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
print(f"----------------")
print(f"Kahn: {kahn_percent:.3%}({khan_votes})")
print(f"Correy: {correy_percent:.3%}({correy_votes})")
print(f"Li: {li_percent:.3%}({li_votes})")
print(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})")
print(f"----------------")
print(f"Winner: {winner_name}")
print(f"----------------")

# Specify File To Write To
output_file = os.path.join('UCBSF201908DATA2' , '01-Lesson-Plans' , '03-Python' , 'Homework' , 'PyPoll' , 'Resources' , 'election_data_analysis_complete.txt')

# txtfile outputs
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"----------------\n")
    txtfile.write(f"Kahn: {kahn_percent:.3%}({khan_votes})\n")
    txtfile.write(f"Correy: {correy_percent:.3%}({correy_votes})\n")
    txtfile.write(f"Li: {li_percent:.3%}({li_votes})\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3%}({otooley_votes})\n")
    txtfile.write(f"----------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"----------------\n")
