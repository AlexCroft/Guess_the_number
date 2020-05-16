import random 

counter = 0
number = random.randint(0,20)
while True:
    counter += 1
    guess = input("Guess the number between 0 and 20: ")
    while True:
        if guess.isnumeric() and int(guess) >= 0 and int(guess) <= 20:
            guess = int(guess)
            break
        else:
            print("{} is not a valid input".format(guess))
            guess = input("Guess the number between 0 and 20: ")
    if  guess != number:
        if guess < number:
            print("To low")
        else:
            print("To high")
    else:
        print("Well done! You complete this in {} tries.".format(counter))
        retry = input("Would you like another game? (y/n): ")
        if retry == 'N' or retry == 'n':
            break
        else:
            counter = 0
            number = random.randint(0,20)