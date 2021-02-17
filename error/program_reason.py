filename = 'reason_file'

with open(filename, 'a') as file_object:
    while True:
        message = input("Why are you like program: ")
        if message == 'quit':
            break
        else:
            file_object.write(message + "\n")