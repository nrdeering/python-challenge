import os
import csv

total_votes = 0

#dictionary for vote count per candidate
vote_count = {}

#path to get data from election_data.csv and outputting it to a text file
election_data = os.path.join('..','PyPoll','election_data.csv')
output_text = os.path.join("PyPoll.txt")

#reader for election_data.csv
with  open(election_data, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header = next(csv_reader)
    
    #loop through rows in election_data.csv, skipping the header 
    for row in csv_reader:
        
        #add up total votes
        total_votes = total_votes + 1
        
        #if steatement that counts the votes per candidate
        if row[2] in vote_count:
            vote_count[row[2]]+=1
            
        else:
            vote_count[row[2]] = 1
            
            
#print results to shell            
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(total_votes))
print("------------------------------")

#for steatemnt that prints name, vote % and vote count by using a key/value pairing from the dictionary
#.items() returns the sequence of tuples in vote_count
for key, value in vote_count.items():
    print(key + ": " + '%.3f' %(vote_count.get(key) * 100/ total_votes) + "% (" + str(value) +")")
print("------------------------------")


#print the winner by finding the max # of votes in the vote count dictionary 
print("Winner: " + max(vote_count, key = vote_count.get))
print("------------------------------")


#write the answers to a text file 
file = open(output_text, "w")
file.write("Election Results\n")
file.write("------------------------------\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("------------------------------\n")
for key, value in vote_count.items():
    file.write(key + ": " + '%.3f' %(vote_count.get(key) * 100/ total_votes) + "% (" + str(value) +")\n")
file.write("------------------------------\n")
file.write("Winner: " + max(vote_count, key = vote_count.get) + "\n")
file.write("------------------------------\n")

file.close()