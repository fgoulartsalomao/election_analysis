#Lists(arrray) users an index, represented by square braces []
    #Declares an empty list counties=[]
    #Add an element to a List - use 'append' / ie.: counties.append("El Paso")
    #Add an element to an specific position on the list: use .insert and define the position and value under () / i.e: counties.insert(2, "El Paso") #2 is the position of the element on the list where you want "El Paso to be at"
  
    #Remove element to a List: use .remove / i.e.: counties.remove("El Paso")
    #Remove an element to an specific position on the list counties.pop(3) #the mumber 3 is the position of the element on the list
    
    #to Change an element on the list at a specific position - counties[2] = "El Paso" "the 2 repesents the position'  

#Tuple - imutable "list" represented by parenteses(or rounded braces)

#Dictionary - an object that stores a collection of data.
    #Has keys and values or key-value pairs
    #Uses the {}
    # on a dictionary conty_dict={'county':'Tombermory} keys=county and value=Tobermory #

#counties_dict={'Guelph':12,'Toronto':55}
#print the value on the given object based on it name
    #print(counties_dict['Toronto'])
    #print(counties_dict.get("Toronto"))
    #print(counties_dict['Toronto'])

#Informs the lenth of dictionary
    #print(len(counties_dict))

#Informs all keys and values from a given dictionaty 
    #print(counties_dict.items())
    
#Informs all the existing keys on the dictionary    
    #print(counties_dict.keys())

#Informs all values on the dict.
    #print(counties_dict.values())


#To verify if variable on list belongs to existing list range.
# If not, then add the new variable to the existing range
# Example: adding new branch  numbers to the list based on a report

#Declares existing list and now list (could also be a value from a dictionary)
# report_list=[2815,2365,2810]
# branch_list = [2815,2365,2330,2390]
# for report in report_list:
#     if report in branch_list:
#         print(f'{report} already exists')
#     else:
#         branch_list.append(report)
# print(f'the new branch list is {branch_list}')

# #To add items from a list to another
# branch_list=[{"Name":"Mississauga","Number":2815},{"Name":"Kitchener","Number":2365},{"Name":"Markham","Number":2810}]
# report_list =[{"Name":"London","Number":2330},{"Name":"Sudbury","Number":2390}]
# for report in report_list:
#     if report_list not in branch_list:
#         branch_list.append(report_list)
# print(branch_list)

#Packages ,Modules,The CSV Module

#1. Open and read a file using open and close functions
        # # Assign a variable for the file to load and the path.
        # file_to_load = './election_results.csv'
        # # Open the election results and read the file.
        # election_data = open(file_to_load, 'r')

        # # To do: perform analysis.

        # # Close the file.
        # election_data.close()

#2. Open and read CVS file using **With** statement
        # import csv

        # with open('./election_results.csv') as election_data:

        # # To do: perform analysis.
        #     print(election_data)

                #Important#
                # 1.Make sure you are under the proper directory *** cd .\Resources\ ***
                # 2. Start typing your file name and press "tab", python will outfill the name for you
                # 2.To run the file (under the proper directory) do as follows " python .\read_file.py "

#3. os = Operations system.