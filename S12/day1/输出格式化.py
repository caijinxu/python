
name = input("you name:").strip("A")
age = int(input("you age:"))
job = input("you job:").strip()
print("information of :%s\nName:%s\nAge:%s\nJob:%s\n"%(name,name,age,job))

'''
%d 整数
%f 浮点数
%s 字符串
%x 十六进制整数

'''
msg = '''
information of :%s
    Name:%s
    Age:%s
    Job:%s
'''%(name,name,age,job)
print(msg)