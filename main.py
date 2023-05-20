import os
import csv
filename='budget_data.csv'
budget_data = os.path.join("Resources","budget_data.csv")
#Variables
total=0
date=[]
months=0
total_months=0
monthly_profit_losses=[]
increase=["",0]
decrease=["",0]
change=0
total_change_profit_losses=0
previous_revenue=0
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    #Read rows of data starting next to header: 
    for row in csvreader:
        date.append(row[0])
        monthly_profit_losses.append(row[1])
        #Total months:
        months+=1
        total_months+= months+int(row[1])
        #Total Change:
        change=int(row[1])-previous_revenue
        if previous_revenue==0:
            change=0
            previous_revenue=int(row[1])
            total_change_profit_losses += change
            #Evaluate Increase
            if change > int(increase[1]):
                increase[1]=change
                increase[0]=row[0]
                #Evaluate Decrease
                if change<int(decrease[1]):
                    decrease[1]=change
                    decrease[0]=row[0]
                    total_change_profit_losses=total_change_profit_losses/(months-1)
               

    # Profit_losses
    # change_profit_losses = int(row[1]) - current_profit_losses
    # current_profit_losses = int(row[1])
    # total = total + current_profit_losses
      
    print(f'Financial Analysis')
    print(f'-----------------------------')
    print(f'Total months: {total_months}')
    print(f'Total: {total_change_profit_losses}')
    print(f'Average change: ${change:.2f}')
    print(f'Greatest Increase in Profits: {increase}')
    print(f'Greatest Decrease in Profits: {decrease}')

   