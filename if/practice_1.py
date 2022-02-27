car = 'audi'
if car == 'subaru':
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("car == 'subaru'")
else:
    print("\nIs car =='audi'? I predict False.")
    print(car == 'audi')
    print("car== 'audi'")


string_1 = 'brother'
string_2 = 'Brother'
if string_1 == string_2.lower():
    print("The two strings are equal.")
else:
    print("The two strings are not equal.")

a = 12
b = 15
#if a == b:
    #print("a = b")
#else :
    #print("a != b")
#if a != b:
    #print(b.upper())
print(a > 16 or b > 16)

players = ['Kobe','James','Jordan','Wade']
player = 'Kobe'
if player not in players:
    print("True")
else:
    print("False")