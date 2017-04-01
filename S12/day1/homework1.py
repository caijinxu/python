d = {'Michael': '95', 'Bob': '75', 'Tracy': '85'}
for i in range(3):
    inname = input("输入你的姓名：")
    if inname in d:
        inpassword = input("输入密码：")
        if inpassword == d[inname]:
            print("欢迎再次登录！")
            break
        else:
            print("密码错误！")
            continue
    else:
        print("请输入正确的用户名！")
if i == 2:
    print("错误输入3次，请稍后再试！")

