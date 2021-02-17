filename = 'The_Last_Leap.txt'
with open(filename) as f_obj:
    contents = f_obj.read()
    words = contents.count('the')
    print(words)