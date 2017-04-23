'''
name = 'enzo'
result = name.__contains__('n')
print (result)
'''

'''
name = 'enzo'
result = name.center(20,'*')
print (result)

'''

'''
name = 'dfajeldsgrjgoreg;goegs;djg'
result = name.count('d',0,10)
print (result)
'''
'''
name = '地方看过'
result = name.encode('gbk')
print (result)
'''
'''
name = 'enzo'
result = name.endswith('z',0,3)
print (result)
'''
'''
#tab换成空格
name = 'enzo\tghh'
result = name.expandtabs()
print (result)
'''
'''
name = 'enzo'
#result = name.find('o')
result = name.index('y')
print (result)
'''
'''
name = 'enzo {0} is {1}'
result = name.format('good','boy')
print (result)


name = 'enzo {name} is {id}'
result = name.format(name ='good',id='boy')
print (result)
'''
'''
li = ['s','b','e','n','s','z']
result = "-".join(li)
print (result)
'''
'''
intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)
str = "this is string example....wow!!!"
print(str.translate(trantab, 'xm'))
'''
'''
#指定字符分割
name = 'enzoissb'
result = name.partition('is')
print (result)
'''
'''
#替换字符
name = 'enzoissb'
result = name.replace('s','o',1)
print (result)

'''


