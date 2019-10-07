#barkochba style number guessing


import random #importing random module 

guesses_taken = 0 #variable with 0 value

print('Hello! What is your name?') #printing string
myName = input() #variable with an input

number = random.randint(1, 20) #variable with generating a random number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #printing name and string

while guesses_taken < 6: #while loop -> while variable's value is less than 6
    print('Take a guess.') #printing string
    guess = input() #variable with input value
    guess = int(guess)#variable with guess value converted to integer

    guesses_taken += 1#variable increased 1

    if guess < number:#if statement -> if the guess variable is less than number variable
        print('Your guess is too low.')#printing string

    if guess > number:#if statement -> if the guess variable is greater than number variable
        print('Your guess is too high.')#printing string

    if guess == number:#if statement -> if the guess variable is equal to number variable
        break#breaking the while loop

if guess == number:#if statement -> if the guess variable is equal to number variable
    guesses_taken = str(guesses_taken)#variable with guesses_taken value converted to string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')#printing name, guesses_taken variable and string

if guess != number:#if statement -> if the guess variable is not equal to number variable
    number = str(number)#variable with number value converted to string
    print('Nope. The number I was thinking of was ' + number)#printing number variable and string
