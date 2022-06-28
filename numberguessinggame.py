import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess the number between 1 and {x}: "))
        if guess>random_number:
            print("sorry your guess was too high")
        elif guess<random_number:
            print("sorry again love your guess was too low")
    print(f"YAYYYYY you guess the correct number {random_number} correctly")

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback !='c':
        if low != high:
            guess=random.randint(low,high)
        else:
            guess=low#could also be high as low=high
        feedback=input(f' if {guess} too high(H),too low(L) or correct(C)??').lower()
        if feedback =='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
    print(f"yayyy the computer guess my number correctly{guess} correctly")
computer_guess(10)