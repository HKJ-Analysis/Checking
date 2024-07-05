mydict = {
    'Fast': 'In a quick manner',
    "Harsh": 'A coder',
    'Marks': [23,45,67],
    
    'anotherdictionary': {'Mom':'love'},
    1: 2
}

# Dictionary Methods
print(mydict.keys())  # Print all keys of dictioonary.
print(mydict.values())  # Print the values of dictionary.

print(mydict.items())   # Prints the (keys,values) of dictionary.

UpdateDict = {
    'Lovish' : 'Friend',
    'Harsh' : 'A Rider'
}
mydict.update(UpdateDict)
print(mydict)

# Get Function

print(mydict.get("Harsh")) # Print valuie associated with key "Harsh"
print(mydict['Harsh'])  # Print valuie associated with key "Harsh"

# The difference between .get() and [] syntax in dictionaries...

print(mydict.get("Harsh2"))     # Returns "None" as "Harsh2" is not present in Dictionary.
print(mydict['Harsh2'])     # Returns "Error" as "Harsh2" is not present in Dictionary.