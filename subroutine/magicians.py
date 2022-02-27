def show_magicians(magicians, great_magicians):
    while magicians:
        current_magician = magicians.pop()
        print("Hello, " + current_magician)
        great_magicians.append(current_magician)

def make_great(great_magicians):
    print("\nThe following magicaians have been modified: ")
    for great_magician in great_magicians:
        print("the Great " + great_magician)

magicians = ['liuqian', 'zhourunfa', 'liming']
great_magicians = []

show_magicians(magicians[:], great_magicians)
make_great(great_magicians)
print("\n")

original_magicians = magicians[:]
show_magicians(original_magicians, great_magicians)
