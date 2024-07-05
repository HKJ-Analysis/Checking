# Q1: Write a program to print the minimum and maximum value in set.

    # a={12,56,34,8,90,1,57}
    # print("The minimum value in sets is :",min(a))
    # print("The maximum value in sets is :",max(a))

# Q2:Write a program to find the common elements in three lists using sets.

# a=[1,5,6,8,2]
# b=[4,5,6,7]
# c=[1,9,6,2,5]

# print(set(a) & set(b) & set(c))


# Q3:Write a program to find difference between two sets.

# a={1,5,6,8,2}
# b={4,5,6,7}

# print(a.difference(b))
# print(b.difference(a))


# Q4: Write a python program to remove an item from a set if it is present in a set.

# a={1,5,6,8,2}
# a.remove(6)
# print(a)

# Q5:Wrie a python program to check if a set is  a subset of another set

b={4,5,6}
c={1,9,6,2,5,4}
print(b.issubset(c))