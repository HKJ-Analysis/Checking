# Example 1: Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# mydict = dict(zip(keys,values))
# print(mydict)


# Exercise 2: Merge two Python dictionaries into one


# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = dict1.copy()
# dict3.update(dict2)
# print(dict3)



# Exercise 3: Print the value of key ‘history’ from the below dict

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict['class']['student']['marks']['history'])



# Exercise 4: Initialize dictionary with default values

# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}


# disc = dict.fromkeys(employees,defaults)
# print(disc)




# Example 5: Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to extract
# keys = ["name", "salary"]

print(sample_dict.items())