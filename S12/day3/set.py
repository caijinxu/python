#set
#s1 = set()
#s1.add('caijinxu')
#s1.add('caijinxu')
#print(s1)
#访问速度快
#天生解决重复问题
# s2 = set(['alex','eric','tony','alex'])
# print(s2)
# s3 = s2.difference(['alex','eric'])
# print(s2)
# print(s3)

# s4 = s2.difference_update(['alex','eric'])
# print(s2)
# print(s4)

# ret = s2.pop()
# print(s2)
# print(ret)

# s2.remove('tony')
# print(s2)

# 练习：寻找差异
# # 数据库中原有
# old_dict = {
#     "#1":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 },
#     "#2":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 }，
#     "#3":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 }
# }
#
# # cmdb 新汇报的数据
#  new_dict = {
#     "#1":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 800 },
#     "#3":{ 'hostname':c1, 'cpu_count': 2, 'mem_capicity': 80 }，
#     "#4":{ 'hostname':c2, 'cpu_count': 2, 'mem_capicity': 80 }
# }
# 1、原来没有==》新加入
# 2、原来有 ==》 更新
#3、新数据有旧数据没有 ==》原来删除
# 三个列表：
#     要更新的数据
#     要删除
#     要添加

# old = set(old_dict.keys())
# new = set(new_dict.keys())
#集合

s1 = set([11,22,33])
s2 = set([22,44])
ret1 = s1.difference(s2)
#difference
ret2 = s1.symmetric_difference(s2)
print(ret1)
print(ret2)