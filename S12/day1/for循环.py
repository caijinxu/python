#猜lucky number
#猜的数字比你的比大小
lucknum = 50
for i in range(3):
    inputnum = int(input("输入一个100以下的数字："))
    if inputnum > lucknum:
        print("太大了")
    elif inputnum < lucknum:
        print("太小了")
    elif inputnum == lucknum:
        print("答对了!")
        break
    #guess_count = guess_count + 1
else:
    print("没有机会了")