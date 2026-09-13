import random

print("="*50)
print("Welcome to the Number Gussing game")
print("="*50)

def choose_difficulty():
    while True:
        difficulty = input("Enter the level of difficulty (easy/medium/hard) : ").lower()
        if difficulty == "easy":
            highest_number = 50
            attempts_limit = 10
            return highest_number, attempts_limit
        elif difficulty == "medium":
            highest_number = 100
            attempts_limit = 7
            return highest_number, attempts_limit
        elif difficulty == "hard":
            highest_number = 200
            attempts_limit = 7
            return highest_number, attempts_limit
        else:
            print("Invalid input")

max_number, max_attempts = choose_difficulty()

while True:
    secret_number = random.randint(1, max_number)
    attempts = 0
    won = False

    while True:
        try:
            guess = int(input("Guess the number : "))
        except ValueError:
            print("Your input was invalid")
            continue
        attempts += 1 # Or attempts = attempts + 1

        if guess < secret_number:
            print("Too low! Try a higher number")
        elif guess > secret_number:
            print("Too high! Try a lower number")
        else:
            print("Your guess was correct!")
            won = True
            break

        if attempts == max_attempts:
            print(f"You are out of attempts , the secret number was : {secret_number}")
            break

    if won:
        print(f"Congratulations you guessed the number in {attempts} attempts!")
    else:
        print(f"Better luck next time, you used all of your {attempts} attempts!")

    play_again = input("Want to play again (y/n) : ")
    if play_again != "y":
        print("="*50)
        print("Thank you for playing this game")
        print("="*50)
        break

    new_difficulty = input("Want to play with the same difficulty or a new difficulty (s/n) : ").lower()
    if new_difficulty == "n":
        max_number, max_attempts = choose_difficulty()