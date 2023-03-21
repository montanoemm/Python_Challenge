#import data from local directory
import os
import csv

#Path to collect data from Resources folder
election_data_csv= os.path.join("Resources","election_data.csv")


#List of values from csv
BallotID=[]
County=[]
Candidate=[]
Charles=[]
Diana=[]
Raymon=[]
votesC=[]
Votes={"Charles Casper Stockham":[Charles],
       "Diana DeGette":[Diana],
       "Raymon Anthony Doane":[Raymon]}
 
#Open and read election data csv
with open(election_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=",")

    #Read the header row first
    csv_header= next(csv_file)

    #Search information skipping the header
    for row in csv_reader:
       
       #Add csv data to python list
       BallotID.append(int(row[0])) 
       County.append(str(row[1]))
       Candidate.append(str(row[2]))
       
    


    #Calculating total votes from list
    NumBallots= len(BallotID)
        
    #Votes per Candidate
    Charles=Candidate.count("Charles Casper Stockham")
    Diana=Candidate.count("Diana DeGette")
    Raymon=Candidate.count("Raymon Anthony Doane")

    
    #Percentage of votes per candidate
    PerCharles= round((Charles/NumBallots)*100,2)
    PerDiana= round((Diana/NumBallots)*100,2)
    PerRaymon= round((Raymon/NumBallots)*100,2)
    #Winner:
    from collections import Counter

    votesC= Counter(Candidate)   
   
    #def Winner(input):
    winner=[]
    for candidate in Votes:
        if Charles > Diana and Raymon:
            winner_count=("Charles Casper Stockham")
        
        elif Diana> Charles and Raymon:
            winner_count=("Diana DeGette")

        elif Raymon> Charles and Diana:
            winner_count=("Raymon Anthony Doane")

            winner.append(str(winner_count))
    


    
    
    
    

#Output data to txt file
Output_P= os.path.join("Resources", "Output_election.txt")

#Open file to write
with open(Output_P, 'w') as textfile:
    textfile.write(f"Election Results\n")
    textfile.write(f"-----------------------------------------------\n")
    textfile.write(f"Total Votes {NumBallots}\n")
    textfile.write(f"-----------------------------------------------\n")
    textfile.write(f"Charles Casper Stockham:{PerCharles}% ({Charles})\n")
    textfile.write(f"Diana DeGette: {PerDiana}% ({Diana})\n")
    textfile.write(f"Raymon Anthony Doane:{PerRaymon}% ({Raymon})\n")
    textfile.write(f"-----------------------------------------------\n")
    textfile.write(f"Winner:{winner_count}\n")
    textfile.write(f"-----------------------------------------------")

print(f"Election Results")
print(f"--------------------------------------------------------------")
print(f"Total Votes: {NumBallots}")
print(f"--------------------------------------------------------------")
print(f"Charles Casper Stockham: {PerCharles}% ({Charles})")
print(f"Diana DeGette: {PerDiana}% ({Diana})")
print(f"Raymon Anthony Doane: {PerRaymon}% ({Raymon})")
print(f"--------------------------------------------------------------")
print(f"Winner: {winner_count}")
print(f"--------------------------------------------------------------")
#print(f"{votesC}")