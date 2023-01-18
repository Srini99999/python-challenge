import os
import csv
import pandas as pd
path = "../../Data/NU-VIRT-DATA-PT-12-2022-U-LOLC/02-Homework/03-Python/Starter_Code/PyPoll/Resources/election_data.csv"

election_df = pd.read_csv(path,encoding="utf8") 

print("ELection  Results")
print("---------------------------------------------------")
votes = election_df["Ballot ID"]
print(f"Total Votes:{len(votes)}")
print("--------------------------------------------------")

print("Charles Casper Stockham :" + str(election_df[election_df.Candidate == "Charles Casper Stockham"]["Ballot ID"].count()/len(votes)* 100)+"(" + str(election_df[election_df.Candidate == "Charles Casper Stockham"]["Ballot ID"].count()
) + ")")

print("Diana DeGette :" + str(election_df[election_df.Candidate == "Diana DeGette"]["Ballot ID"].count()/len(votes)* 100)+"(" + str(election_df[election_df.Candidate == "Diana DeGette"]["Ballot ID"].count()
) + ")")


print("Raymon Anthony Doane:" + str(election_df[election_df.Candidate == "Raymon Anthony Doane"]["Ballot ID"].count()/len(votes)* 100)+"(" + str(election_df[election_df.Candidate == "Raymon Anthony Doane"]["Ballot ID"].count()
) + ")")

print("--------------------------------------------------")

print(f" Winner is : {election_df['Candidate'].value_counts().idxmax()}")
