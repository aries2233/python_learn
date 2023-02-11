from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def knn_iris_gscv():
    #1 获取数据
    iris=load_iris()
    #2 数据集划分
    x_train,x_test,y_train,y_test=train_test_split(iris.data, iris.target,random_state=6)
    #3 标准化
    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.transform(x_test)#用x_train的fit结果
    #4 KNN算法预估器
    estimator = KNeighborsClassifier()
    # 加入网格搜索与交叉验证
    param_dict = {"n_neighbors":[1,3,5,7,9,11]}
    estimator=GridSearchCV(estimator,param_grid=param_dict,cv=10)
    estimator.fit(x_train,y_train)
    #5 模型评估
    #法1 对比真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n",y_predict)
    print("直接比对真实值和预测值：\n",y_test == y_predict)
    #法2 计算准确率
    score = estimator.score(x_test,y_test)
    print("准确率：\n",score)

    #最佳参数：best_params_
    print("最佳参数：\n",estimator.best_params_)
    #最佳结果：best_score_
    print("最佳结果：\n", estimator.best_score_)
    #最佳预估器：best_estimator_
    print("最佳预估器：\n", estimator.best_estimator_)
    #交叉验证结果：cv_results_
    print("交叉验证结果：\n", estimator.cv_results_)
    return None

knn_iris_gscv()
