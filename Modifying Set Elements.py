data = input("Enter list elements separated by space: ")
lst = data.split()

new = set()
for item in lst:
    new.add(item)

print("Set after removing duplicates:", new)

def add(s):
    element = input("Enter element to add: ")
    s.add(element)
    print("Updated set:", s)

def remove(s):
    element = input("Enter element to remove: ")
    if element in s:
        s.remove(element)
        print("Element removed")
    else:
        print("Element not found")
    print("Updated set:", s)

add(new)
remove(new)
