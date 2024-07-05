student = { "name":"John" , "class": "6th", "roll_no":24 }
# print(student["name"])
# print(student["class"])
# print(student["roll_no"])



# Print all keys of dictionary.
# for x in student:
#     print(x)


# Print all the key values.

# for x in student:
#     print(student[x])


# Using Value function 

for x in student.values():
    print(x)


# Using items function

for x,y in student.items():
    print(x,y)