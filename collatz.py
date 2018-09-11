def collatz(i):
    x=round(i)
    if x%2==0:
        print(round(x/2))
    else:
        print(round(x*3+1))
while True:
    try:
        i=int(input())
        collatz(i)
        break 
    except:
        print("Enter integer values")
        continue
