#import dependencies
import os
import csv

#set variables
Total_months = 0
Total = 0
Avg_change = []
Monthly_count = []
Greatest_increase = 0
Greatest_decrease = 0
Profit_loss_current = 0
Profit_loss_previous = 0
Profit_loss_change = 0

#set path for csv file
Budget_path = os.path.join("../PyBank/Resources/budget_data.csv")

#read csv files
with open(Budget_path) as Budget_file:
    reader = csv.reader(Budget_file, delimiter = ",")

#read header first
header_csv = next(Budget_file)

print(f"Header: {header_csv}")

#go through the rows
for row in Budget_path:
    Total_months +=1
#calcualte net total amount
Monthly_decrease = int(row[1])
Avg_change += Monthly_decrease


#make previous month equal to current
if (Monthly_count == 1):
    Profit_loss_previous = Profit_loss_current


else:

#calculate profit Loss change
    Profit_loss_change = Profit_loss_current - Profit_loss_previous

# Append the Months
    Monthly_count.append(row[0])
# Append each profit_loss_change to the Avg_change[]
    Avg_change.append(Profit_loss_change)

# Make the Profit_loss_current to be Profit_loss_previous for the next loop
    Profit_loss_previous = Profit_loss_current

#sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(Monthly_count - 1), 2)
# highest and lowest changes in "Profit/Losses" over the entire period
    Greatest_increase = max(profit_loss_changes)
    Greatest_decrease = min(profit_loss_changes)

# Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    Greatest_month_index = Avg_change.index(Greatest_increase)
    Greatest_loss_month_index = Avg_change.index(Greatest_decrease)

# Assign best and worst month
    best_month = Monthly_count[Greatest_month_index]
    worst_month = Monthly_count[Greatest_loss_month_index]

#Print in terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {Monthly_count}")
print(f"Total:  ${Total}")
print(f"Average Change:  ${Avg_change}")
print(f"Greatest Increase in Profits:  {best_month} (${Greatest_increase})")
print(f"Greatest Decrease in Losses:  {worst_month} (${Greatest_decrease})")



#export text files
Budget_file = os.path.join("Output", "budget_data.txt")
with open(Budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {Monthly_count}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${Avg_change}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${Greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${Greatest_decrease})\n")
