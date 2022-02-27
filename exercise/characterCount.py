import pprint
message = 'I am wangyuankun and 27 years old!'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(someDictionaryValue)
