'''

dic = {'k1':'v1','k2':'v2'}
#print(dic['k1'])
#print(dic['k2'])
#print(dic['k3'])
print(di c.get('k1'))
print(dic.get('k2'))
print(dic.get('k3','somebody'))
'''

'''
dic = {'k1':'v1','k2':'v2'}
print(dic.keys())
print(dic.items())
print(dic.values())
'''
#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
#即： {'k1': 大于66 , 'k2': 小于66}

dic = {}
all_list = [11,22,33,44,55,66,77,88,99,90]
for i in all_list :
    if i>66:
        if "k1" in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1']=[i,]
    else:
        if "k2" in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i,]
print(dic['k1'])
print(dic['k2'])