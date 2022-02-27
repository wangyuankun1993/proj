file_name = 'guest.txt'
with open(file_name, 'r+') as file_object:
    while True:
        name_message = input("请输入你的名字：")
        if name_message == 'quit':
            break
        elif name_message == 'cls':
            file_object.truncate()
            break
        else:
            file_object.write("My name is " + name_message + "\n")