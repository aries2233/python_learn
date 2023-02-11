import defs,os

while 1:
    num=0
    choices=defs.play()
    print("开始进行测试...")
    while 1:
        tick=0
        num=num+1
        temp=defs.run()
        for check in choices.values():
            if check in temp:
                tick=tick+1
            else:
                 break
        if tick==5:
            break
    defs.end(num)
    e=input("退出系统请输入q或Q，输入其他再次进行模拟 ")
    if e=="q" or e =="Q":
        exit(0)
    print("\n")
