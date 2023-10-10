#reading data information
import csv
import os
import math


#declaring variables
count=0

total=0
Profit_Loss= []
Net_Change_List= []
Previous_Profit_Loss = 0
Greatest_Increase = 0
Greatest_Increase_Month = ""
Greatest_Decrease= 0
Greatest_Decrease_Month = ""



#reading CSV file
with open('C:\\Users\\diann\\OneDrive\\Documents\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv', mode = 'r') as file:
    csvFile = csv.reader(file)


#List Profits and Profit Changes
    header=next(csvFile)
    firstrow=next(csvFile)
    Previous_Profit_Loss = int(firstrow[1])
    Profit_Loss.append(int(firstrow[1])) 
    count +=1
    for lines in csvFile:
        count +=1
        print(lines[0])
        #Net_change calculation
        Net_Change= int(lines[1]) - Previous_Profit_Loss
        Net_Change_List.append(Net_Change)
        #finding previous_loss
        Previous_Profit_Loss = int(lines[1])
        Profit_Loss.append(int(lines[1]))
        #finding maximum_profit
        if Net_Change > Greatest_Increase:
            Greatest_Increase = Net_Change
            Greatest_Increase_Month = lines[0]

        if Net_Change < Greatest_Decrease:
            Greatest_Decrease = Net_Change
            Greatest_Decrease_Month = lines[0]  

        #Maximum_Profit = max(Net_Change_List)
        #finding max profit date
        #Maximum_Profit_Date= Maximum_Profit.cell(row=row, column=column-1)
        #Decrease_Profit = min(Net_Change_List)
        #finding decreased profit date
        #Decrease_Profit_Date = Decrease_Profit.cell(row=row, column=column-1)
    

Date = 0
pro_loss=1


#printing results
#print('Financial Analysis')

#print('-----------------------------------')

#print total months in data
#print('Total Months:', count)

# #print total profit list from data
# print ('Total:', sum(Profit_Loss))

# #print average change in profit
Average= sum(Net_Change_List)/ len(Net_Change_List)
# print('Total:', Average)

# #print greatest increase/decrease in profits with date and totals
# print('Greatest Increase in Profits:', Greatest_Increase_Month, Greatest_Increase)
# print('Greatest Decrease in Profits:', Greatest_Decrease_Month, '$'(Greatest_Decrease))

output = f"""
Financial Analysis
----------------------------
Total Months: {count}
Total: ${sum(Profit_Loss)}
Average Change: ${Average:.2f}
Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase})
Greatest Decrease in Profits: {Greatest_Decrease_Month} (${Greatest_Decrease})
"""

print(output)

with open('C:\\Users\\diann\\OneDrive\\Documents\GitHub\\python-challenge\\PyBank\\analysis\\budget_data', "w") as textfile:
    textfile.write(output)