data1 = input("Enter elements of first set separated by space: ")
set1 = set(data1.split())

data2 = input("Enter elements of second set separated by space: ")
set2 = set(data2.split())

print("Intersection:", set1.intersection(set2))
print("Union:", set1.union(set2))
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2.difference(set1))
