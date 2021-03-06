# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0

# Candidate options
candidate_options = [] 

#Declare an empty dictionary
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election resutls and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # add to the total vote count
        total_votes = total_votes + 1
    
        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking the candidate vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to the candidate count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#Save results to text file
with open(file_to_save, "w") as txt_file:

#Print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    
    #Save final vote count to text file
    txt_file.write(election_results)
    
    #Determine the % of votes for each candidate by looping throug the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count for a candidate
        votes = candidate_votes[candidate_name]

        #calculate % of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # #print candidate name and % of votes
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        #Print each candidate's name, vote count, and % votes to terminal
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
      
        #Save candidate results to text file
        txt_file.write(candidate_results)

        #Determine winning vote count and candidate
        #determine if the votes are greater than the winning count
        if(votes>winning_count) and (vote_percentage>winning_percentage):
            #If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to the candidate name
            winning_candidate = candidate_name

    #Winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    #Save winning candidate name to text file
    txt_file.write(winning_candidate_summary)

# #Print the candidate vote directory
# print(candidate_votes)

# #Print the candidate list
# print(candidate_options)

# #print total votes
# print(total_votes)  






 
