secret_number = 4
guess_limit = 3
guess_count = 0

while guess_count < guess_limit:
    guess = int(input("Guess Number:"))
    guess_count += 1
    if guess == secret_number:
        print("You WON")
        break
else:
    print("You Failed")