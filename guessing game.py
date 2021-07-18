import random
x = int(input("Low a number: "))
y = int(input("High a number: "))
the_number = random.randint(x, y)
guess = int(input("Guess a number between "+ str(x) +" and " + str(y)+ " : "))
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again")
    if guess < the_number:
        print(guess, "was too low. Try again.")
    guess = int(input("Guess again: "))
print(guess, "was the number! You win!")
