def sum1(d):
    return sum(d.values())
n = int(input("Enter a number n: "))
dict1 = {}
for x in range(1, n + 1):
    dict1[x] = x ** 2
print("Generated Dictionary:")
print(dict1)
total = sum1(dict1)
print("Sum of all values in dictionary:", total)
