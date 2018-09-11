import re, pyperclip
pregex=re.compile(r'''
                      (\d{3}|\(\d{3}\))?
                      (\-|\s|\.)?
                      (\d{3}|\(\d{3}\))
                      (\-|\s|\.)
                      (\d{4}|\(\d{4}\))''',re.VERBOSE)
eregex=re.compile(r'''
                      (\w+)
                      \@
                      (\w+)
                      \.
                      (\w{3,5})''')
text=str(pyperclip.paste())

print(pregex.findall(text))
print(eregex.findall(text))
