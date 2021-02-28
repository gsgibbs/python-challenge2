#import dependencies
import os
import csv

#Define path
election_path = os.path.join("../Pypoll/Resources/election_data.csv")

#set variables
total_number_votes = 0
list_candidates = []
dictionary_candidates = {}
winning_vote = 0
election_winner = ""

#open/read csv file
with open(election_path, newline="") as election_file:
    election_reader = csv.reader(election_file, delimiter=",")
    reader = csv.reader(election_file)
    next(reader, None)

for row in reader:

# count total votes
    total_number_votes += 1

#reference candidate name
candidate_name = row[2]

#create if statement
if candidate_name not in candidate_list:

#add candidate to list
    list_candidates.append(candidate_name)
    dictionary_candidates[candidate_name] = 0
    dictionary_candidates[candidate_name] +=1


#export text files
output = 'Analysis/election_results.txt'
with open(output, "w", newline="") as votefile:

#print total number of total_number_votes

    print(f"Election Results")
    print(f"--------------------")
    print(f"Total Votes: {total_number_votes}")
    print(f"--------------------")

    votefile.write(f"Election Results\n")
    votefile.write(f"--------------------\n")
    votefile.write(f"Total Votes: {total_number_votes}\n")
    votefile.write(f"--------------------\n")


#loop and calculate percentage
for candidate_name in dictionary_candidates:
    percentage = round(float(dictionary_candidates[candidate_name])/float(total_number_votes),2)
    print(f"{candidate_name}: {percentage:.3%} ({dictionary_candidates[candidate_name]})\n")
        votefile.write(f"{candidate}: {percentage:.3%} ({dictionary_candidates[candidate_name]})\n")

votes = dictionary_candidates[candidate_name]
if votes > winning_vote:
winning_vote = votes
election_winner = candidate_name

# print to terminal/txt file
    print(f"--------------------")
    print(f"Winner: {election_winner}")
    print(f"--------------------")
    votefile.write(f"--------------------\n")
    votefile.write(f"Winner: {election_winner}\n")
    votefile.write(f"--------------------")
