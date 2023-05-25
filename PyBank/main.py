import os
import csv

filename = 'budget_data.csv'
budget_data = os.path.join("budget_data.csv")
pathout = os.path.join("Analysis", "budget_data.txt")

# Variables
total_months = 0
total_profit_losses = 0
monthly_profit_losses = []
change_profit_losses = []
date = []

with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    previous_profit_losses = 0
    for row in csvreader:
        
        # Total months:
        total_months += 1

        # Total profit/losses:
        current_profit_losses = int(row[1])
        total_profit_losses += current_profit_losses

        # list of monthly profit/losses:
        monthly_profit_losses.append(current_profit_losses)
        
        # Total change in profit/losses:
        if previous_profit_losses != 0:
         
            change_profit_losses.append(current_profit_losses - previous_profit_losses)
            # Updating previous profit/losses:
            previous_profit_losses = current_profit_losses
            date.append(row[0])
        else:
            previous_profit_losses = current_profit_losses    
            # Average change:

    #print(change_profit_losses)        
    average_change = sum(change_profit_losses) / len(change_profit_losses)
                    
    # Greatest increase and Greatest decrease in profits/losses:
    greatest_increase = max(change_profit_losses)
    greatest_decrease = min(change_profit_losses)

    # Dates for Greatest increase and Greatest decrease in profits/losses:
    increase_index = change_profit_losses.index(greatest_increase)
    decrease_index = change_profit_losses.index(greatest_decrease)
    greatest_increase_date = date[increase_index + 1]
    greatest_decrease_date = date[decrease_index + 1]

# Financial Analysis:
print("Financial Analysis")
print("-----------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}")

#Text file with the results 
with open(pathout, "w") as Analysis:
    Analysis.write(f"Financial Analysis\n")
    Analysis.write("-----------------------------\n")
    Analysis.write(f"Total months: {total_months}\n")
    Analysis.write(f"Total: ${total_profit_losses}\n")
    Analysis.write(f"Average change: ${average_change:.2f}\n")
    Analysis.write(f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase}\n")
    Analysis.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease}\n")