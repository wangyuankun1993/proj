with open('python_learning_report.txt') as file_object:
    # contents = file_object.read()
    # print(contents)
    # for line in file_object:
    #     print(line.rstrip())
    lines = file_object.readlines()
    for line in lines:
        message = line.replace('Python', 'C')
        print(message)