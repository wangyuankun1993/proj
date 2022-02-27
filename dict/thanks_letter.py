thanks_members = {
    'liming':'c',
    'zhangfei':'python',
    'liubei':'java',
    'guanyu':'php',
}
for name in sorted(thanks_members.keys()):
    print(name.title())
if 'zhaoyun' not in thanks_members.keys():
    print("Zhaoyun, please take our poll!")