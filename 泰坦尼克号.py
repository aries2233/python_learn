import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#读取数据
fp=r"D:\Python\项目\泰坦尼克号\data\titanic\train.csv"
data = pd.read_csv(fp,engine="python",encoding='gbk',usecols=[0,1,2,3,4,5,7])
#清洗数据
data['Age']=data['Age'].fillna(data['Age'].mean())#缺失年龄用平均年龄替代
#筛选性别数据
#sexdata = data.iloc[:,[1,4]]
#print(sexdata)
#性别与存活率数据
mnum=(len(data[data.Sex=='male']))
fnum=(len(data[data.Sex=='female']))
print(mnum)
print(fnum)
msnum=(len(data[(data.Sex=='male')&(data.Survived==1)]))
print(msnum)
fsnum=(len(data[(data.Sex=='female')&(data.Survived==1)]))
print(fsnum)
ms=msnum/mnum
print(round(ms,2))
fs=fsnum/fnum
print(round(fs,2))
#转换为numpy数组
#malearray = np.array(sexdata[sexdata["Sex"]=="male"])
#print(len(malearray))
#绘图
#男性存活情况
plt.figure(figsize=(10, 5))
plt.style.use('fivethirtyeight')
malet=["Number of male deaths","Number of male survivors"]
malen=[mnum-msnum,msnum]
plt.pie(malen,labels=malet,autopct='%1.2f%%',startangle=90,explode=[0.1,0])
#plt.pight_layout()
plt.title('Male survival')
plt.show()
#女性存活情况
plt.figure(figsize=(10, 5))
plt.style.use('fivethirtyeight')
femalet=["Number of female survivors","Number of female deaths"]
femalen=[fsnum,fnum-fsnum]
plt.pie(femalen,labels=femalet,autopct='%1.2f%%',explode=[0.1,0],colors=['r', 'c'])
#plt.pight_layout()
plt.title('Female survival')
plt.show()
#存活率对比
plt.figure(figsize=(10, 5))
plt.style.use('fivethirtyeight')
sex_x=["Male","Female"]
srate_y=[ms,fs]
plt.bar(sex_x,srate_y,label="Survival rate")
plt.legend()
plt.show()