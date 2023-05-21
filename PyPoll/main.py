import os 
import csv

csvpath = os.path.join("Resources", "election_data.csv")
pathout = os.path.join("Analysis", "election_results.txt")

# Variables to store data
candidates=[]
votes=[]
county=[]
Charles_Casper_Stockham=[]
Diana_DeGette=[]
Raymon_Anthony_Doane=[]

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
	if can=="Charles_Casper_Stockham":
		Charles_Casper_Stockham.append(candidates)
		votes_Charles_Casper_Stockham=len (Charles_Casper_Stockham)
	elif can=="Diana_DeGette":
		Diana_DeGette.append(candidates)
		votes_Diana_DeGette=len(Diana_DeGette)
		can=="Raymon_Anthony_Doane"
		Raymon_Anthony_Doane.append(candidates)
		votes_Raymon_Anthony_Doane=len(Raymon_Anthony_Doane)

# The percentage of votes each candidate won.
per_Charles_Casper_Stockham=round(((votes_Charles_Casper_Stockham/votes_total)*100), 2) 
per_Diana_DeGette=round(((votes_Diana_DeGette/votes_total)*100), 2)
per_Raymon_Anthony_Doane=round(((votes_Raymon_Anthony_Doane/votes_total)*100), 2)


# The winner of the election based on popular vote. 
def winner (candidates):
	return max(set (candidates), key=candidates.count)

# Print the analysis to the terminal.

print(f'Election Results')
print('------------------')
print(f'Total votes: {votes}')
print(f'-----------------')
print(f'Charles_Casper_Stockham: %{per_Charles_Casper_Stockham} {votes_Charles_Casper_Stockham}')
print(f'Diana_DeGette: %{per_Diana_DeGette} {votes_Diana_DeGette}')
print(f'Raymon_Anthony_Doane: %{per_Raymon_Anthony_Doane} {votes_Raymon_Anthony_Doane}')
print('------------------')
print(f'Winner: {winner}')
print('-------------------')

# Text file with the results 
with open(pathout, "w") as results:
	results.write(f"Election Results\n")
	results.write("----------------------\n")
	results.write(f"Total votes: {votes}\n")
	results.write(f"----------------------\n")
	results.write(f"Charles_Casper_Stockham: %{per_Charles_Casper_Stockham} ({votes_Charles_Casper_Stockham})\n")
	results.write(f"Diana_DeGette: %{per_Diana_DeGette} ({votes_Diana_DeGette})\n")
	results.write(f"Raymon_Anthony_Doane: %{per_Raymon_Anthony_Doane} ({votes_Raymon_Anthony_Doane})\n")
	results.write("----------------------")
	results.write(f"Winner: ({winner})\n")
	results.write(f"----------------------")