import random

secretNumber = random.randint(1, 5)
print('i am thinking of a number between 1 to 5 ')

# ask a plyer to guess
for guessesTaken in range(1, 4):
    print('take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')

    elif guess > secretNumber:
        print('your guess is too high')

    else:
        break

if guess == secretNumber:
    print('you are the ultimate winner!!')
    print('Good job! you guessed secret number in ' + str(guessesTaken) + ' ' + 'guesses!')

else:

    print('Nop! The number I was thinking ' + str(guessesTaken))
