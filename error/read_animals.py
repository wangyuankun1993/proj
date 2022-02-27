def open_file(filename_x):
    try:
        with open(filename_x) as f_object_n:
            content=f_object_n
    except FileNotFoundError:
        print('404 not found!')
    else:
        print(content.rstrip())

animal_list=['cats.txt', 'dogs.txt']
for i in animal_list:
    open_file(i)