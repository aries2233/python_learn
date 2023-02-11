from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

#读取数据
iris=load_iris()
#划分数据集
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,random_state=22)
#决策树预估器
estimator=DecisionTreeClassifier(criterion="entropy")
estimator.fit(x_train,y_train)
#模型评估
#比对真实值和预测值

y_predict = estimator.predict(x_test)

print("y_predict:\n",y_predict)

print("直接对比真实值和预测值:\n",y_test == y_predict)

#计算准确率

score = estimator.score(x_test,y_test)

print("准确率为:\n",score)

#可视化决策树
export_graphviz(estimator,out_file="iris_tree.dot",feature_names=iris.feature_names)