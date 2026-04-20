data1 = input("Enter elements of first set separated by space: ")
set1 = set(data1.split())

data2 = input("Enter elements of second set separated by space: ")
set2 = set(data2.split())

if set1.issubset(set2):
    print("First set is subset of second set")
elif set2.issubset(set1):
    print("Second set is subset of first set")
else:
    print("No subset relation between the sets")
