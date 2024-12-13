# list1 = [2, 51, 11, 13, 51, 100]
# 1. Output every item from list with positive indexing.
# 2. Output every item from list with negative indexing.
# 3. Replace the last element of a list with a new value.
# 4. Replace the fifth element of a list with a new value.


list1 = [2, 51, 11, 13, 51, 100]

for i in range(len(list1)):
    print(f"Index {i}: {list1[i]}")

print("----")


for i in range(-1, -len(list1)-1,-1):
    print(f"Index {i}: {list1[i]}")


print("----")
list1[-1] = 200
print(list1)

print("----")
list1[-2] = 250
list1[4] = 250
print(list1)
