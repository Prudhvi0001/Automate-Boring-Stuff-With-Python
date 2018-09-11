import random
secrectnumber=random.randint(0,20)
print("guess a number b//w (1,20) ")
for guessnumber in range(1,7):
    print("guess a number")
    guess=int(input())
    if guess > secrectnumber:
        print("your guess is too high")
    elif guess<secrectnumber:
        print("your guess is too low")
    else:
        break
if guess==secrectnumber:
    print("you guessed my number in",str(guessnumber),"guess")
else:
    print("nope i was thinking about",str(secrectnumber))
