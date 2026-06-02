# For loop with range
print("=== For loop with range ===")
for i in range(5):
    print(f"Iteration {i}")

# For loop with list
print("\n=== For loop with list ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# For loop with enumerate (get index and value)
print("\n=== Enumerate ===")
for index, fruit in enumerate(fruits, start=0):
    print(f"{index}. {fruit}")

# While loop
print("\n=== While loop ===")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1


