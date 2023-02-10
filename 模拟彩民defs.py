import random

tips = "这是一个11选5彩票模拟系统"
tips += "\n您可以从1~11中选择5个数字"
tips += "\n通过抽取数字估算获得大奖的预期期数"
s=list(range(1,12))

def play():
    c={1:0,2:0,3:0,4:0,5:0}
    print(tips)
    for step in range(1, 6):
        tips1 = "请输入第"
        tips1 += str(step)
        tips1 += "个数字 "
        while 1:
            choice = int(input(tips1))
            if choice in s:
                if choice in c.values():
                    print("该数字已输入，请重新输入 ")
                else:
                    c[step] = choice
                    break
            else:
                print("数字不在范围内，请重新输入 ")
    print("您选择了以下数字：")
    for num in c.values():
        print(num)
    return c

def run():
    temp=[]
    for step in range(1, 6):
        while 1:
            t=random.randint(1,11)
            if t in temp:
                1
            else:
                temp.append(t)
                break
    return temp

def end(x):
    tips2="您预计会在第"
    tips2+=str(x)
    tips2+="期获得大奖"
    print(tips2)
