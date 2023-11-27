import random

def guess(number):
    if number==number_to_guess:
        print("Your guess is correct, you won")
        return True
    else:
        if number>number_to_guess:
            print("To high")
        elif number<number_to_guess:
            print("To low")
    print("Guess again")
    return False


print("Welcom to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("Chose a difficluty. Type 'easy' or 'hard': ")

live=1
if difficulty == "hard":
    live = 5
elif difficulty == "easy":
    live = 10

number_to_guess = random.randint(1, 100)

while(live>0):
    if guess(int(input("Make a guess: "))):
        break
    else:
        live-=1
        print(f"You have {live} attempts remaing to guess")
    if(live==0):
        print("You have run out of guess, you lose")
