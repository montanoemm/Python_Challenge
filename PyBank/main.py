#import data from local directory
import os
import csv

#Path to collect data from Resources folder
budget_data_csv= os.path.join("Resources", "budget_data.csv")

#List of values from csv
Dates=[]
ProfitLos=[]
monthly_change=[] 
#Open and read budget data csv
with open(budget_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    #Read the header row first
    csv_header= next(csv_file)

    previous_profit=1088983
    monthcount=0
    #Search information skipping the header
    for row in csv_reader:
       
       #Determine profit values
       #Add csv data to python list
       Dates.append(row[0]) 
       ProfitLos.append(int(row[1]))
       
       
             
            
    #Create functions
       #def Adding_all(lst)
           #pos_sum= 0
           #neg_sum= 0           
       monthcount=monthcount+1
       current_profit=int(row[1])
       #Total_profit= Total_profit + current_profit
       change=current_profit - previous_profit
       
       monthly_change.append(change)
       previous_profit= current_profit


             
    #Calculating totals from list
    NumMonths= len(Dates)
    
    #Add values
    
    Total_sum= sum(ProfitLos)
    Format_Total_Sum= "${:,.2f}".format(Total_sum)
    #mean value
    #Average=(Total_sum)/NumMonths
    #Average=(change/NumMonths)*100
    #Format_Average="${:,.2f}".format(Average)
    
    Average_Change=sum(monthly_change)/(len(monthly_change)-1)
    F_Average="${:,.2f}".format(Average_Change)

    #Dictionary
    new_dict=dict(zip(Dates,monthly_change))
    find_max=max(new_dict,key=new_dict.get)
    find_min=min(new_dict,key=new_dict.get)

    #Greatest Increase in Profits:
    #GreatestInc= max(ProfitLos)
    #Format_GreatInc="${:,.2f}".format(GreatestInc)
    AGreatInc= max(monthly_change)
    FAGreatInc="${:,.2f}".format(AGreatInc)
    

    #Greatest Decrease in Profits:
    #GreatestDec= min(ProfitLos)
    #Format_GreatDec="${:,.2f}".format(GreatestDec)
    AGreatDec= min(monthly_change)
    FtAGreatDec="${:,.2f}".format(AGreatDec)

#Output data to txt file
Output_P= os.path.join("Resources", "Output_budget.txt")

#Open file to write
with open(Output_P, 'w') as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"--------------------------------------------------\n")
    textfile.write(f"Total Months {NumMonths}\n")
    textfile.write(f"Total: {Format_Total_Sum}\n")
    textfile.write(f"Average Change: {F_Average}\n")
    textfile.write(f"Greatest Increase in Profits: {find_max} {FAGreatInc}\n")
    textfile.write(f"Greatest Decrease in Profits: {find_min} {FtAGreatDec}\n")

#print to terminal
print(f"Financial Analysis")
print(f"---------------------------------------")
print(f"Total Months: {NumMonths}")

print(f"Total: {Format_Total_Sum}")
#print(f"Average Change: {Format_Average}")
print(f"Average Change: {F_Average}")

#print(Dates)
#print(ProfitLos)
#print(f"Greatest Increase: {Format_GreatInc}")
#print(f"Greatest Decrease: {Format_GreatDec}")
print(f"Greatest Increase:  {find_max} {FAGreatInc}")
print(f"Greatest Decrease: {find_min} {FtAGreatDec}")
#print(type(ProfitLos))
#print(change)
#print(monthly_change)