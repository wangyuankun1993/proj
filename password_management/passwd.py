_user = "wangyuankun"
_passwd = "wangyuankun1993"

count = 0
while count <5:
    name = input("Please input your name:")
    passwd = input("Please input your password:")
    if name == _user and passwd == _passwd:
        print("Welcome %s to here!" % name)
        break
    else:
        print("Invalid username or password!")
        print("Please try again!")
    count += 1
print("Please try after 5 minutes again!")
