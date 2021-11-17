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

#add the dependencies
import csv
import os
# Assign a variable to load(read) a file from a path.
file_to_load=os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis","election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Uses read and analyze the data
    file_reader=csv.reader(election_data)
        # Print each row in the CSV file.
    #for row in file_reader:
        print(row)
        
        # to print based on the position(i.e: first item on each row) use the index for each row (printed as list)
        #print(row[0])
    
        #to print the header only
        # headers= next(file_reader)
        # print(headers)