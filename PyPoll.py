# Add dependencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Create a candidate list
candidate_options =[]
# Create a candidate votes dictionary
candidate_votes={}
# Winning candidate and winning count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0 
# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read header row
    headers =next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes +=1
        # Get the candidate name from each row
        candidate_name = row[2]
        # If the candidate name does not match any candidate name in the candidate options list
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate options list
            candidate_options.append(candidate_name)
            # Track candidate vot count
            candidate_votes[candidate_name] = 0
        # Add votes to corrsponding candidate name
        candidate_votes[candidate_name] += 1
    # Save the results to our text file
    with open(file_to_save, "w") as txt_file:
        # Print to the text file
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file
        txt_file.write(election_results)
        # Loop through candidate list
        for candidate in candidate_votes:
            # Retrieve total votes of each candidate
            votes = candidate_votes[candidate]
            # Calculate each candidate precentage of votes
            vote_percentage = float(votes)/float(total_votes) * 100
            # Print each candidate name, votes, and percentage of votes
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
            #Print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)
            #Save the candidate results to the text file
            txt_file.write(candidate_results)
            # Determine if the votes is greater than the winning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true, set winning_candidate equal to that candidate's name
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate
        # Print the winning candidate summary
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}5\n"
            f"-------------------------")
        print(winning_candidate_summary)
        # Save the winning candidate summary to the text file
        txt_file.write(winning_candidate_summary)