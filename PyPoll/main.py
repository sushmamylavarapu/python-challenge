import os 
import csv
import numpy

csvpath = os.path.join("election_data.csv")
pathout = os.path.join("Analysis", "election_results.txt")

# Variables to store data
candidates=[]
votes=[]
county=[]
Charles_Casper_Stockham=[]
Diana_DeGette=[]
Raymon_Anthony_Doane=[]
votes_Charles_Casper_Stockham=0
votes_Diana_DeGette=0
votes_Raymon_Anthony_Doane=0

#create three columns: 
with open(csvpath) as csvfile:
	csvreader=csv.reader(csvfile, delimiter=',')
	csv_header=next(csvreader)

#Read each row of data after the header and loop through rows
	for row in csvreader:
		votes.append(row[0])
		county.append(row[1])
		candidates.append(row[2])
		
# The total number of votes cast   
votes_total=len(row[1])


# A complete list of candidates who received votes and the
for can in candidates:
	
	if can=="Charles Casper Stockham":
		Charles_Casper_Stockham.append(can)
		
	elif can=="Diana DeGette":
		Diana_DeGette.append(can)
	else:	
		Raymon_Anthony_Doane.append(can)
		
votes_Charles_Casper_Stockham=len (Charles_Casper_Stockham)
votes_Diana_DeGette=len(Diana_DeGette)
votes_Raymon_Anthony_Doane=len(Raymon_Anthony_Doane)

# The percentage of votes each candidate won.
per_Charles_Casper_Stockham=round(((votes_Charles_Casper_Stockham/len(votes))*100), 2) 
per_Diana_DeGette=round(((votes_Diana_DeGette/len(votes))*100), 2)
per_Raymon_Anthony_Doane=round(((votes_Raymon_Anthony_Doane/len(votes))*100), 2)


# The winner of the election based on popular vote. 
candidateList=["Charles_Casper_Stockham", "Diana_DeGette", "Raymon_Anthony_Doane"]
resultList=[votes_Charles_Casper_Stockham, votes_Diana_DeGette, votes_Raymon_Anthony_Doane]
index=numpy.argmax(resultList)
winner=candidateList[index]

# Print the analysis to the terminal.

print(f'Election Results')
print('------------------')
print(f'Total votes: {len(votes)}')
print(f'-----------------')
print(f'Charles_Casper_Stockham: %{per_Charles_Casper_Stockham} {votes_Charles_Casper_Stockham}')
print(f'Diana_DeGette: %{per_Diana_DeGette} {votes_Diana_DeGette}')
print(f'Raymon_Anthony_Doane: %{per_Raymon_Anthony_Doane} {votes_Raymon_Anthony_Doane}')
print('------------------')
print(f'Winner: {winner}')
print('-------------------')

# Text file with the results 
with open(pathout, "w") as election_results:
	election_results.write(f"Election Results\n")
	election_results.write("----------------------\n")
	election_results.write(f"Total votes: {votes}\n")
	election_results.write(f"----------------------\n")
	election_results.write(f"Charles_Casper_Stockham: %{per_Charles_Casper_Stockham} ({votes_Charles_Casper_Stockham})\n")
	election_results.write(f"Diana_DeGette: %{per_Diana_DeGette} ({votes_Diana_DeGette})\n")
	election_results.write(f"Raymon_Anthony_Doane: %{per_Raymon_Anthony_Doane} ({votes_Raymon_Anthony_Doane})\n")
	election_results.write("----------------------")
	election_results.write(f"Winner: ({winner})\n")
	election_results.write(f"----------------------")