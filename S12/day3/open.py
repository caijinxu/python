#写入文件
#f = open('test.log','w')
#f.write('fjdioaijfengoirjgierj')
#f.close()
#读取2个字节
f = open('test.log','r')
# ret = f.read(3)
# print(ret)
'''
print(f.tell())#c查看当前指针位置
f.read(2)

print(f.tell())
'''
f.seek(6)
print(f.read())
f.close()
