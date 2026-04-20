def check(d, key):
    if key in d:
        print("Key exists in the dictionary.")
    else:
        print("Key does not exist in the dictionary.")
dict1 = {}
n1 = int(input("Enter number of elements in first dictionary: "))
for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value
dict2 = {}
n2 = int(input("Enter number of elements in second dictionary: "))
for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value
new = dict1.copy()
new.update(dict2)
print("Concatenated Dictionary:")
print(new)
search = input("Enter key to search: ")
check(new, search)
