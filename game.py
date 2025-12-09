import random

lower_num=1
higher_num=1000
answer = random.randint(lower_num,higher_num)
guessess = 0
is_running = True

print("welcome to number guessing game")
print(f"select a  number between{lower_num} and {higher_num}")
while is_running:
    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guessess += 1
        if guess < lower_num or guess > higher_num:
            print("that number is out of range.try again")
            print(f"select a  number between{lower_num} and {higher_num}")
        elif guess <answer:
            print("too low,try again")
        elif guess > answer:
            print("too high ,try again")
        else:
            print(f"congratulations! you guessed the number {answer} in {guessess} guesses.")
            is_running = False
    else:
        print("inavalid guess")
        print(f"select a  number between{lower_num} and {higher_num}")