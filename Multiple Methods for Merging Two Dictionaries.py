dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 200, "d": 40}
print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)
merged1 = dict1.copy()
merged1.update(dict2)
print("1. Using update():", merged1)
merged2 = dict1.copy()
merged2.update(dict2)
print("2. Using update() function:", merged2)
merged3 = dict1.copy()
for key, value in dict2.items():
    merged3[key] = value
print("3. Using for loop:", merged3)
