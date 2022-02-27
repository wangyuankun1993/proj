current_users = ['liuchunyu','wangyuankun','liming','zhangfei','guanyu']
new_users = ['Liuchunyu','wangyuankun','liubei','caocao','zhaoyun']
for user in new_users:
    if user.lower() in current_users:
        print("Please input another user.")
    else:
        print("The user can be used.")