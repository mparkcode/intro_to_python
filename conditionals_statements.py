# age = 16

# if age >= 18:
#     print('You are an adult')
# else:
#     print('You are a minor')

# grade, >=90 A , >= 80B , >= 70 C , >= 60 D, F

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}") 

# Nested conditionals
temperature = 25
is_raining = False

if temperature > 20:
    if is_raining:
        print("It's warm but raining. Bring an umbrella!")
    else:
        print("Perfect weather for a walk!")
else:
    print("It's quite cold outside.")