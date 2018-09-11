def isphonenumber(number):
    if len(number) != 12:
        return False
    if not number[0:3].isdecimal():
        return False
    if number[3] != '-':
        return False
    if not number[4:7].isdecimal():
        return False
    if number[7] != '-':
        return False
    if not number[8:13].isdecimal():
        return False
    return True
print('is it a phone number or not')
print('455-555-9999 is pn:', isphonenumber('455-555-9999'))
print('mos-ifg-uhrf is pn:', isphonenumber('mos-ifg-uhrf'))
message='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    if isphonenumber(message[i:i+12]):
        print(message[i:i+12])
print("Done numbers found!")
