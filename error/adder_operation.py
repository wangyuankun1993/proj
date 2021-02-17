while True:
    try:
        inp_a=input("请输入数字：")
        inp_a_to_int=int(inp_a)
        inp_b=input("请输入数字：")
        inp_b_to_int=int(inp_b)
    except ValueError:
        print("只能输入整型")
    else:
        print(inp_a_to_int+inp_b_to_int)
        break