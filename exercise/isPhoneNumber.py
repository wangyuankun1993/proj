import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 411-555-1101 tomorrow. 411-345-1000 is my office number.'
for i in range(len(message)):
    list = message[i:i+12]
    if isPhoneNumber(list):
        print('Phone number found: ' + list)
print('Done')

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 411-334-1030, 123-4325-2314.')
mo1 = phoneNumRegex.findall('My number is 411-334-1030, 123-4325-2314.')
print(mo)
print(mo1)
