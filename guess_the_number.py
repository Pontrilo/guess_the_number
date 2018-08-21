#  Mini-game of guessing the random number that the program picks.

import random  # Allows the use of random number picking.

minimum = 1
maximum = 20
max_guesses_allowed = 10
target_number = random.randint(minimum, maximum)  # Generates the random number.
print("""The target number is between {} and {},
you have {} guesses to find it... """.format(minimum, maximum, max_guesses_allowed))

for guesses in range(1, max_guesses_allowed + 1):
    while True:  # This block prevents people guessing strings or anything outside the
        try:     # range.
            initial_guess = (int(input("What's your guess?: ")))
        except ValueError:
            print("I'm sorry you have to enter a number or press CTRL + F2 to exit ")
            continue
        if initial_guess < minimum or initial_guess > maximum:
            print("You must pick within the range! or press CTRL + F2 to exit ")
            continue
        else:
            break

# This block tells the player if they are higher or lower than the target.

    if initial_guess > target_number:
        print("Your guess is too high, try again!")
    elif initial_guess < target_number:
        print("Your guess is too low, try again!")
    else:
        break

# This final block tells you whether you guessed the target in the allowed amount of
# guesses or not.

if initial_guess == target_number:
    print("\ncongrats you got it in {} guesses!".format(guesses))
else:
    print("\nUnlucky, the number I picked was {}".format(target_number))
