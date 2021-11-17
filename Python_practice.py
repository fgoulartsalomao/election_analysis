# counties = ['Arapahoe','Denver','Jefferson']
# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is  in the list of counties.")
# else:
#     print("Arapahoe is  in the list of counties and El Paso is not in the list of counties.")


#testing while loops
# counties = ['Arapahoe','Denver','Jefferson']
# for county in counties:
#     print(county)

# numbers=[0,1,2,3,4]
# for num in numbers:
#     print(num)

#testing range()
# counties_tuple=("arapahoe","Denver","Jefferson")
# for i in range(len(counties_tuple)):
#     print(counties_tuple[i])

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county)

#get value on dictionary
# for voters in counties_dict.values():
#     print(voters)

#Print key and value
# for county, voters in counties_dict.items():
#     print(county,voters)


#Print key and value as text message
# for county, voters in counties_dict.items():
#     print(str(county)+' county has '+str(voters)+' voters.')

#Use tange to iterate over the list of dictionaries and print the counties in voting_data
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
# for i in range(len(voting_data)):
#     print(voting_data[i])

#To print the keys and then values of each dictionary that belong to a list
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
# for county in voting_data:
#     for value in county.values():
#         print(value)

#To print the registered_voters of each dictionary that belong to a list
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
# # for i in range(len(voting_data)):
# #   if (i==0):
# #         print(i)
# for registered_voters in voting_data[:-1]:
#   for value in registered_voters.values():
#     print(value)
        # # second test - To print the registered_voters number of each dictionary that belong to a list
        # voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
        # #county_dict is to makes reference of the the object (in this the dictionary)
        # for county_dict in voting_data:
        #   print(county_dict['registered_voters'])


# To print the county name from each dictionary that belongs to a list
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353},{"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print(county_dict['county'])

#Code without f-strings
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

#code using f-strings
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#3.2.11
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

#Example witout f-string (traditional)
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

#Example with f-strings (new)
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

#practice for f-string
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# print(message_to_candidate)

#Fixing floating-point decimals on f-string: add ":,)" for separator and ":.2f)"  for two decimals
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# print(counties_dict["Denver"])

   #3.4.1 Import the datetime class from the datetime module.
    # import datetime as dt
    # # Use the now() attribute on the datetime class to get the present time.
    # now = dt.datetime.now()
    # # Print the present time.
    # print(f"The time right now is ", now)
  
#to concatenate string and value on print message
        # counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

        # for county, voters in counties_dict.items():
        # #Conventional concatenation
        # #print(county + " county has " + str(voters) + " registered voters.")
        # #Concatenation with F-string
        #         print(f"{county} county has {voters:,} registered voters.")

#Print key values from each dictionary inside a list
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
#Create a loop to execute the print for each dictionary inside my list
        #data = each dictionary existent on my list
        #voting data = List of dictionaries
for data in voting_data:
        print(f"{data['county']} county has {data['registered_voters']:,} registered voters")