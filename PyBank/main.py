#importing the modules 
import os
import csv
import pandas as pd
import pandas as pd


path = "../../Data/NU-VIRT-DATA-PT-12-2022-U-LOLC/02-Homework/03-Python/Starter_Code/PyBank/Resources/budget_data.csv"
# read the CSV file 
budget_df=pd.read_csv(path,encoding="utf8")
# print the total months"
print(f"Total Months:{len(budget_df.Date)}")

numbers=budget_df["Profit/Losses"]
# calculatioing the average

def average(nums):
    sum = 0
    for num in numbers:
        sum = sum + num
    return sum/len(nums)
	

# print the average value
print(f"Average Change : {average(numbers)}")

# print the Greatest increase and decrease in profits)
print((f"Greatest Increase in Profits:{budget_df.Date.loc[numbers.idxmax()]}") +"(" +(f"{numbers.max()}") + ")")
print((f"Greatest Decrease in Profits:{budget_df.Date.loc[numbers.idxmin()]}") +"(" +(f"{numbers.min()}") + ")")
