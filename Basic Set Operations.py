def create():
    data = input("Enter integers separated by space: ")
    numbers = data.split()
    s = set()
    for num in numbers:
        s.add(int(num))
    print("Set:", s)
    print("Length of set:", len(s))
    return s
def print1(s):
    print("Elements in the set:")
    for item in s:
        print(item)
def check(s):
    element = int(input("Enter element to check: "))
    if element in s:
        print("Element exists in the set")
    else:
        print("Element does not exist in the set")
set1= create()
print1(set1)
check(set1)
