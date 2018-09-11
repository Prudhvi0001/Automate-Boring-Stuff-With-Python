#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import re, pyperclip
#phoneNumRegex
phoneNumRegex=re.compile(r'''((\d{3}|\(\d{3}\))?
                        (\s|\.|\-)?()
                        (\d{3})
                        (\s|\.|\-)
                        (\d{4})
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?
                        )''',re.VERBOSE)
#emailRegex
emailRegex=re.compile(r'''(
            [a-zA-Z0-9.% +-]+
            @
            [a-zA-Z0-9.-]
            (\.[a-zA-Z]{2,4})
            )''',re.VERBOSE)
text=str(pyperclip.paste())
matches=[]
for groups in phoneNumRegex.findall(text):
    phonenumber='-'.join([groups[1],groups[3],groups[5]])
    if groups[8]!='':
        phonenumber+=' x'+groups[8]
    matches.append(phonenumber)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print("no number or email is found")
