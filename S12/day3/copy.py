import copy
# #浅拷贝
# copy.copy()
# #深拷贝
# copy.deepcopy()
# #赋值
#
# a1 = 123123
# # a2 = 123123
# # a2 = a1
# # print(id(a1))
# # print(id(a2))
# a3 = copy.deepcopy(a1)
# print(id(a1))
# print(id(a3))

dic = {
    "cpu":[80,],
    "men":[80,],
    "disk":[80,]
}
print('befor',dic)
new_dic = copy.copy(dic)
new_dic["new"][0] = 50
print(dic)
print(new_dic)