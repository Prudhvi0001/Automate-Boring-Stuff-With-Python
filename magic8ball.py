import random
def magic8ball(b):
    if b==1:
        return 'you are damm'
    elif b==2:
        return 'two square'
    elif b==3:
        return 'you hit the jackpot'
    elif b==4:
        return 'you got an another chance'
    elif b==5:
        return 'you must do a frog walk'
    elif b==6:
        return 'you are sexy'
    elif b==7:
        return 'best of luck'
    elif b==8:
        return 'king is on his way'

x=random.randint(1,9)
print(magic8ball(x))
