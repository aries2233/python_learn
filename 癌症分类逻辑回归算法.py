++++++import pandas as pd
import numpy as np
#获取数据
column_name = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
               'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin',
               'Normal Nucleoli', 'Mitoses', 'Class']
data=pd.read_csv(r"D:\Python\项目\癌症分类逻辑回归算法\venv\癌症分类.data",names=column_name)
#数据处理（缺失值）
data=data.replace(to_replace="?",value=np.nan)
data.dropna(inplace=True)
data.isnull().any()
#数据集划分
from sklearn.model_selection import train_test_split
x=data.iloc[:,1:-1]
y=data["Class"]
x_train,x_test,y_train,y_test=train_test_split(x,y)
#特征工程————无量纲化：标准化
from sklearn.preprocessing import StandardScaler
transfer=StandardScaler()
x_train=transfer.fit_transform(x_train)
x_test=transfer.transform(x_test)
#逻辑回归预估器
from sklearn.linear_model import LogisticRegression
estimator=LogisticRegression()
estimator.fit(x_train,y_train)
#逻辑回归的模型参数：回归系数和偏置
print("回归系数:\n",estimator.coef_)
print("偏置:\n",estimator.intercept_)
#模型评估
#比对真实值和预测值
y_predict = estimator.predict(x_test)
print("y_predict:\n",y_predict)
print("直接对比真实值和预测值:\n",y_test == y_predict)
#计算准确率
score = estimator.score(x_test,y_test)
print("准确率为:\n",score)
#查看精确率、召回率、F1-score
from sklearn.metrics import classification_report
report=classification_report(y_test,y_predict,labels=[2,4],target_names=["良心","恶性"])
print(report)
#将y_test转换成0或1
y_true=np.where(y_test>3,1,0)
from sklearn.metrics import roc_auc_score
roc=roc_auc_score(y_true,y_predict)
print("ROC:\n",roc)