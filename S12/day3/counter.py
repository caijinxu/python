import  collections
obj = collections.Counter('dfewhfiwefiepsdhpwe')
print(obj)
ret = obj.most_common(4)
print(ret)
"""elements() 计数器中的所有元素，注：此处非所有元素集合，而是包含所有元素集合的迭代器 """
for k in obj.elements():
    print(k)
#items 迭代字典内容
for k,v in obj.items():
    print(k,v)
