from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Ridge

def linear3():
    #岭回归
    #获取数据集
    boston=load_boston()
    #划分数据集
    x_train,x_test,y_train,y_test=train_test_split(boston.data,boston.target,random_state=22)
    #特征工程：无量纲化-标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)
    #预估器
    estimator=Ridge(alpha=0.5,max_iter=10000)
    estimator.fit(x_train,y_train)
    #得出模型
    print("岭回归权重系数:\n",estimator.coef_)
    print("岭回归偏重:\n",estimator.intercept_)
    #模型评估
    y_predict=estimator.predict(x_test)
    print("岭回归预测房价:\n",y_predict)
    error=mean_squared_error(y_test,y_predict)
    print("岭回归均方误差:\n",error)
    return None

linear3()#岭回归