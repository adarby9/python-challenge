import csv
import os
datafile=os.path.join("Resources","budget_data.csv")
with open(datafile) as file:
   reader=csv.reader(file)
   header=next(reader)
   ##data=list(reader)

   total_months=86 
   row1=next(reader)
   print (row1)
   total_profit_loss=row1[1]
   previous_profit_loss=int(row1[1])
   changes=[]
   dates=[]

   for row in reader:
    date=row[0]
    total_month=total_months+1
    profit_loss=int(row[1])-previous_profit_loss
    print(profit_loss)
    previous_profit_loss=int(row[1])
    print(previous_profit_loss)
    total_profit_loss=int(row1[1])

    if previous_profit_loss!=0:
      change=profit_loss-previous_profit_loss
      changes.append(change)
      dates.append(date)
print(changes)

previous_profit_loss=profit_loss

net_total=total_profit_loss
average_change=sum(changes)/len(changes)

max_increase=max(changes)
max_decrease=min(changes)
max_increase_date = dates[changes.index(max_increase)]
max_decrease_date = dates[changes.index(max_decrease)]

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})")   