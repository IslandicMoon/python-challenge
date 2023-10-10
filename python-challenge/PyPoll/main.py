#reading data information
import csv

total_votes= 0

#obtain data into list
candidate_list = []
candidate_votes = {}


with open('C:\\Users\\diann\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\election_data.csv', mode = 'r') as file:
    csvFile = csv.reader(file)

    

    header = next(csvFile)

    #obtain candidate votes
    for lines in (csvFile):
        candidate= lines[2]
        total_votes += 1
        
        if candidate not in candidate_list:

            candidate_list.append(candidate) 
            candidate_votes[candidate] = 0

        candidate_votes[candidate] += 1

with open('C:\\Users\\diann\\OneDrive\\Documents\GitHub\\python-challenge\\PyPoll\\analysis\\election_data', "w") as textfile: 
    y= (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

    print(y)

    textfile.write(y)   

    max_votes = 0
    winner = ""   
    
    for candidate in candidate_list:
        votes = candidate_votes[candidate]
        percent = votes / total_votes * 100

        output = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(output)

        textfile.write(output)

        if votes > max_votes:
            max_votes = votes
            winner = candidate
            
    result = ("Winner:" + winner)

    
    print(result)

    textfile.write(result)