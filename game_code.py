correct_numbers = [42, 18, 77]
game_records = []

# Write your code here:
for number in correct_numbers:
    guess_count = 0
    print("\nGuess the number between 1 and 100.")

    while True:
        user_input = input("Enter your guess: ")
        guess = int(user_input)
        guess_count += 1

        if guess < number:
            print("Too low! Try again.")
            print(guess_count)
        elif guess > number:
            print("Too high! Try again.")
            print(guess_count)
        elif guess == number:
            print(f"Correct! The number was {number}.")
            print(guess_count)
            break
        else:
            if guess_count == 3:
                break

    game_records.append(guess_count)

print("\nGame Summary:")
for i, guesses in enumerate(game_records):
    print(f"Round {i + 1}: {guesses} guesses")