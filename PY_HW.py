import os
import csv

#Set Path
csvpath = os.path.join("Resources", "budget_data.csv")

#Open CSV 
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


    #print(f"CSV Header: {csv_header}")

#Count month and Profit/Loss
    month_count = 0
    total_pl = 0
    number_value = []
    month_list = []
    first_row = next(csvreader)
    previoius_profit_loss = int(first_row[1])
    print(previoius_profit_loss)
    print(type(previoius_profit_loss))
    month_count = month_count + 1
    total_pl += int(first_row[1])
    for row in csvreader:
        month_count = month_count + 1
        total_pl += int(row[1])
        number_value.append(int(row[1]))
        month_list.append(row[0])
        change = int(row[1]) - previoius_profit_loss
        previoius_profit_loss = int(row[1])
    max_value_index = number_value.index(max(number_value))
    min_value_index = number_value.index(min(number_value))
    Month_Max = month_list[max_value_index]
    Month_Min = month_list[min_value_index]



    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(month_count))
    print("Total Profit: " + str(total_pl))
    print("Average Change:", previoius_profit_loss/int(month_count))
    print("----------------------------")
    print("Greatest Increase in Porfits {} {}".format(Month_Max, max(number_value)))
    print("Greatest Decrease in Porfits {} {}".format(Month_Min, min(number_value)))