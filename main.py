import random

upp_limit = int(input("Enter the upper range of the number"))

if upp_limit <= 0:
    print("Please enter a number greater than 0.")
    quit()

r = random.randint(0,upp_limit)

tot_guess = 0

while True:
    tot_guess += 1
    user_res = int(input("Make a guess for the number"))

    if user_res == r:
        print("You got it!")
        break
    else:
        if user_res > r:
            print("Guess Some smaller number!")
        else:
            print("Guess Some larger number.")

    if tot_guess >= 10:
        print("Guess ran out.")
        break

print(f"You got it in {tot_guess} guess.")
