
'''
f = open("test.log","w")

f.write("第一行\n")
f.write("第2行\n")
f.write("第3行\n")
f.write("最后一行\n")

f.close()

'''

'''
f = open("test.log","r")
for line in f:
    if "3" in line:
        print ("this is the 3 line")
    else:
        print (line),
f.close()
'''
'''
f = open("test.log","w")
f.write("8")
f.write("9")
f.close()
'''

f = open("test.log","w")
f.write("")