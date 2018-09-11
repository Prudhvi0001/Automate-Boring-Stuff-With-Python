#! python3
# passwordmanager.py - An insecure password locker program.
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
import sys, pyperclip
account=sys.argv[1]
if len(sys.argv)<2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print(account,"password is copied to clipboard")
else:
    print("their is no password")
