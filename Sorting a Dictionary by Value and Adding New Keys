def add(d):
    key = raw_input("Enter key to add: ")
    value = int(input("Enter value: "))
    d[key] = value
dict1 = {
    "a": 50,
    "b": 20,
    "c": 40
}
print("Original Dictionary:")
print(dict1)
sorted1 = dict(sorted(dict1.items(), key=lambda item: item[1]))
print("Dictionary sorted by value:")
print(sorted1)
add(dict1)
print("Dictionary after adding new key:")
print(dict1)
sorted2 = dict(sorted(dict1.items(), key=lambda item: item[1],reverse=True))
print("Dictionary sorted again by value:")
print(sorted2)
