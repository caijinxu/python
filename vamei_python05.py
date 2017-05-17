ta = [1,2,3]
tb = [9,8,7]

# cluster
zipped = zip(ta,tb)
print((zipped))

# decompose
na, nb = zip(*zipped)
print(na, nb)

def f(x):
    x[0] = 100
    print (x)

a = [1,2,3]
f(a)
print (a)