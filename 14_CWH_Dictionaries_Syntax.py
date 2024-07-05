mydict = {
    'Fast': 'In a quick manner',
    "Harsh": 'A coder',
    'Marks': [23,45,67],
    
    'anotherdictionary': {'Mom':'love'}
}

print(mydict['Fast'])
print(mydict['Harsh'])

mydict['Marks'] = [45,76] # Mutable Dictionary
print(mydict['Marks'])

print(mydict['anotherdictionary'])
print(mydict['anotherdictionary']['Mom'])