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

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Candidate options and candidate votes.
county_options = []
county_votes = {}

# Variables for winning candidate and county, final count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_county= 0
winning_c_percentage=0

# Declares variables to diplay the largest county and county voter turnout.
lrg_turnout_county = ""
lrg_turn_count = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.

    for row in file_reader:
        # Add one value to the total_vote variable until the end of the file (count)
        total_votes += 1
        # Get the candidate name from each row using index of the file row.
        candidate_name = row[2]
        # Get the county name from each row using index of the file row.
        county_name = row[1]
        # Verifies if the candidate is already on the list (duplicated or not), then add to it (if not duplicated)
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate_options list.
            candidate_options.append(candidate_name)
            # Set all candidate ote count variable to 0 before start collecting data from file.
            candidate_votes[candidate_name] = 0
        # Stores one vote to the give candidate on the dictionary at a time (will repeat through the loop).
        # candidate_votes[key] +=1 (value to be added)
        candidate_votes[candidate_name] += 1
        
        
        if county_name not in county_options:
            
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0


        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Saves the results to the determined text file.

#Statement to open the file as w = write
with open(file_to_save, "w") as txt_file:
    #Declares variable to be used to print and write the election results (total of votes)
    election_results = (
        f"\n**Election Results**\n"
        f"-----------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------------\n\n"
        f"Details per County:\n"
        f"-------------------------------\n")
    #prints total_votes variable created on Terminal
    print(election_results, end="")
    # Writes and save the count votes to the text file using data storaged in the election_results variable (above)
    txt_file.write(election_results)

    #For loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(county) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {county:,} | {county_percentage:.1f}%\n")

         # 6d: Print the county results to the terminal.
        print(county_results, end="")
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county > winning_county) and (county_percentage > winning_c_percentage):
            winning_county = county
            winning_c_candidate = county_name
            winning_c_percentage = county_percentage

    #Prints the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"\nCounty Summary:\n"
        f"---------------------------------\n"
        f"Largest County Turnout: {winning_c_candidate}\n"
        f"Winning County Vote: {winning_county:,}\n"
        f"Winning County Percentage: {winning_c_percentage:.1f}%\n\n"
        f"Percentage of Votes per Candidate:\n"
        f"-----------------------------------\n")

    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)



    #Iterates through the each candidate (key) in the dictionary candidates_votes in order to:
        # create variable for votes
        # Calculate the %
        # Print the name > vote % and qty of votes for each.
    for candidate_name in candidate_votes:
        # Creates variable for the votes count
        votes = candidate_votes[candidate_name]
        #calculates the %
        vote_percentage = float(votes) / float(total_votes) * 100
        #variable for the string
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% | {votes:,}\n")
        # Prints the string in the vasriable  (each candidate's votes count and percentage to the terminal)
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determines the winner by checking if votes of the current candidate been checked are > than the previous
        # If condition is true, then will storage votes, the % and candidate name to variables
        # those variables were already declared before reading the file and set as = 0
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (

        f"\nWinner Summary:\n"
        f"-----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n\n"
        f"---------------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)