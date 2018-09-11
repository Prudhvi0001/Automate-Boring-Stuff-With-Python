birthdays={'prudhvi':'jun24','surya':'jun5','dinesh':'sep30'}
while True:
    print("enter the name:(nothing to quit)")
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(name," date of birth is",end='')
        print(' ',birthdays[name])
    else:
        print("Your name is not on the list")
        bday=input("enter your DOB:")
        birthdays[name] = bday
        print("your name is updated")
