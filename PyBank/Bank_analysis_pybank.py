# Importing OS and CSV
import os
import csv

# Variable list
total_months = 0
net_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# data source location
csvpath = os.path.join('UCBSF201908DATA2' , '01-Lesson-Plans', '03-Python' , 'Homework' , 'PyBank' , 'Resources' , 'budget_data.csv')


with open(csvpath, newline='') as csvfile:

    # list the delimiter
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    row = next(csvreader)

    # setting result fields for assignment output
    previous_row = int(row[1])
    total_months += 1
    net_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]

    # Read Each Row Of Data After The Header
    for row in csvreader:


        total_months += 1
        net_amount += int(row[1])

        # month to month change
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])


        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]


        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

# printout
print(f"Financial Analysis")
print(f"________________")
print(f"Total Months: {total_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# writing files 72-84
output_file = os.path.join('UCBSF201908DATA2' , '01-Lesson-Plans', '03-Python' , 'Homework' , 'PyBank' , 'Resources' , 'budget_data_analysiscomplete.txt')


with open(output_file, 'w',) as txtfile:

    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"________________\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
