file_name = 'guest_book.txt'
with open(file_name, 'r+') as file_object:
    while True:
        message = input("Please input your name:")
        if message == 'quit':
            break
        else:
            file_object.write("Welcome " + message + "!" + "\n")
            print("Hello " + message + ".")