fruits = ['apple', 'banana', 'cherry']
# print(f"Original List: {fruits}")

# Accessing elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modifying lists
print(f"Before append: {fruits}")
fruits.append('grape')
print(f"After append: {fruits}")

fruits.insert(1, "avocado")
print(f"After insert: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

# List methods
print(f"Length: {len(fruits)}")
print(f"Count of 'apple': {fruits.count('apple')}")
fruits.insert(3, "apple")
print(f"Count of 'apple': {fruits.count('apple')}")