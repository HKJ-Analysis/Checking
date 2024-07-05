b=set()
print(type(b))

 # ADD METHOD

b.add(7)
b.add(2)
b.add(5)
b.add(5) 

# b.add([4,8,9]) Unhasable Type lists cannot use in sets 

# b.add({4:2}) Cannot add dictionary in sets

b.add((1,8,9)) #But we can hash tuple in same format with () bracket

print(b)
print(len(b))


 # REMOVE METHOD 

# b.remove(5)
# print(b)


 # POP METHOD

# b.pop()  # Will pop any element not fixed
# print(b)

 # CLEAR METHOD

# b.clear()
# print(b)


 # COPY METHOD

a=b.copy()
print(a)

set1={"Ironman","Hulk","Thor","Captain-America"}
set2={"Superman","Batman","Wonder-Woman"}
set3={"Hulk","Thor"}

 #isdisjoint()

print(set2.isdisjoint(set1)) # No element of set2 present in set1 so it will give True

print(set1.isdisjoint(set3)) # One element of set3 is present in set1 so it will give False.