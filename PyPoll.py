#The Data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

#1. Use of OS to open a file creating a indirect path

#import csv
# import os

# file_to_load=os.path.join("Resources","election_results.csv")
# print(file_to_load)
# with open(file_to_load) as election_data:
#     print(election_data)

#2. 3.4.3 - Write to Files with Python

#A-using OPEN and CLOSE

    # import csv
    # import os

    # # Create a file name variable to a direct or indirect path to the file.
    # file_to_save = os.path.join("analysis","election_analysis.txt")

    # # Uses an open statement to open the file as a text file.
    # outfile = open(file_to_save, "w")

    # # Write some data to the file.
    # outfile.write("Hello World")

    # # Close the file
    # outfile.close()

#B-using WITH

        # #add the dependencies
        # import csv
        # import os

        # # Create a file name variable to a direct or indirect path to the file.
        # file_to_save=os.path.join("analysis","election_analysis.txt")

        # # Using the with statement open the file as a text file.
        # with open(file_to_save, "w") as txt_file:

        #     # Write some data to the file.
        #     # txt_file.write("Arapahoe, Denver, Jefferson")
        #     #Use \n to perform write each data that's separated by coma on a separate line
        #         txt_file.write("Counties.in.the.Election\n-------------------------\nArapahoe\nDenver\nJefferson")

# 3.4.4 Read the Election Results

# #add the dependencies
# import csv
# import os
# # Assign a variable to load(read) a file from a path.
# file_to_load=os.path.join("Resources","election_results.csv")
# # Assign a variable to save the file to a path.
# file_to_save=os.path.join("analysis","election_analysis.txt")

# # Open the election results and read the file.
# with open(file_to_load) as election_data:


#     #Uses read and analyze the data
#     file_reader=csv.reader(election_data)
#     # Uses a loop print each row in the CSV file.
#     for row in file_reader:
#         print(row)
        
#         # to print based on the position(i.e: first item on each row) use the index for each row (printed as list)
#         #print(row[0])
    
#         #to print the header only
#         # headers= next(file_reader)
#         # print(headers)

#         # #to skip the header, declare next(file_reader) before the loop as follows:
#         # next(file_reader)
#         # with open(file_to_load) as election_data:
#         #     print(row)

# #3.5.1 - using the file to perform counts - total votes

        # # Add our dependencies.
        # import csv
        # import os
        # # Assign a variable to load a file from a path.
        # file_to_load = os.path.join("Resources", "election_results.csv")
        # # Assign a variable to save the file to a path.
        # file_to_save = os.path.join("analysis", "election_analysis.txt")

        # # 1. Initialize a total vote counter.
        # total_votes = 0

        # # Open the election results and read the file
        # with open(file_to_load) as election_data:
        #     file_reader = csv.reader(election_data)

        #     # Read the header row.
        #     headers = next(file_reader)

        #     # Print each row in the CSV file.
        #     for row in file_reader:
        #         # 2. Add to the total vote count.
        #         total_votes += 1

        # # 3. Print the total votes.
        # print(total_votes)

#3.5.2 - Get the Candidates in the Election


# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Declare a new list to store the candidates
candidate_options = []
#Declare an empty distionary to use for counting the votes for each candidate
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Creates a variable for the candidate name and informs the index on the row (list), which is column 3 (count start on 0)
        candidate_name = row[2]
    # Conditional to check if the candidate is not yet in the list
        if candidate_name not in candidate_options:
        
        # If condition is true, then the below adds the candidate name to the list candidate_options
            candidate_options.append(candidate_name)
            # Starts candidate_votes at 0 value
            candidate_votes[candidate_name]=0
        # Starts inscreasing the value of cadidate_votes by 1 for each row it finds it
        candidate_votes[candidate_name] +=1

# Print the candidate list.
print(f'The candidates who particiapted in this election were: {candidate_options}.')
print(f'The total of votes in the electoin was of {total_votes:,} votes.')
# print(f'Here are each canditate votes: {candidate_votes}')

# for loop to iterate through each canditate in the list
for candidate_name in candidate_options:
#retrieves the count of votes for a candidate at a time
    votes=candidate_votes[candidate_name]
#creates a variable to storage the percentage cancutation for each candidate at a time
    vote_percentage=float(votes)/float(total_votes)*100
        #Prints the % result for each candidate at a time
        #print(f'{candidate_name}: received {vote_percentage:.2f}% of the votes')

    #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #to determine the winning candidate
    #Check if votes are greater then
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary=(
    f'----------------------------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count: {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'----------------------------------------------\n')
print(winning_candidate_summary)