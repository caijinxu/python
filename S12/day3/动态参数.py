s1 = '{0} is {1}'
l = [ 'ab','cd','ss']
result = s1.format(*l)
print(result)
s2 = "{name} is {bba}"
D1 = {'name':'caij','bba':'love'}
result = s2.format(**D1)
print(result)