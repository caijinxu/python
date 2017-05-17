def func(a,b,c):
    print (a,b,c)

args = (1,3,4)
func(*args)
dict = {'a':1,'b':2,'c':3}
func(**dict)

S = 'abcdefghijk'
for i in range(0,len(S),2):
    print (S[i])
for (index,char) in enumerate(S):
    print (index)
    print (char)