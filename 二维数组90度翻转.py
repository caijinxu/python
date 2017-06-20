#!/usr/bin/python
# -*- coding: utf-8 -*-

data=[[i for i in range(4)] for raw in range(4)]
for ele in data:
    print ele
a=len(data)
for i in range(a):#外层循环
    for j in range(i+1,len(data[i])): #内层循环
        #交换数据
        temp=data[i][j]
        data[i][j]=data[j][i]
        data[j][i]=temp
for ele in data:
    print ele