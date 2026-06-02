# String creation and concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# String formatting
age = 30
message = f"{first_name} is {age} years old"
print(message)

# String slicing
text="Python Programming"
print(f"First 6 characters: {text[:6]}")
print(f"Last 11 characters: {text[-11:]}")
print(f"Every 2nd character: {text[::2]}")

# String methods
sample = "  hello world  "
print(f"Original: '{sample}'")
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Capitalize: {sample.capitalize()}")
print(f"Strip: '{sample.strip()}'")
print(f"Replace: {sample.replace('world', 'Python')}")
print(f"Split: {sample.split()}")
