from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error

def linear1():
    #正规方程
    #获取数据集
    boston=load_boston()
    #划分数据集
    x_train,x_test,y_train,y_test=train_test_split(boston.data,boston.target,random_state=22)
    #特征工程：无量纲化-标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)
    #预估器
    estimator=LinearRegression()
    estimator.fit(x_train,y_train)
    #得出模型
    print("正规方程权重系数:\n",estimator.coef_)
    print("正规方程偏重:\n",estimator.intercept_)
    #模型评估
    y_predict=estimator.predict(x_test)
    print("正规方程预测房价:\n",y_predict)
    error=mean_squared_error(y_test,y_predict)
    print("正规方程均方误差:\n",error)
    return None

def linear2():
    #梯度下降
    #获取数据集
    boston=load_boston()
    #划分数据集
    x_train,x_test,y_train,y_test=train_test_split(boston.data,boston.target,random_state=22)
    #特征工程：无量纲化-标准化
    transfer=StandardScaler()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)
    #预估器
    estimator=SGDRegressor(learning_rate="constant",eta0=0.01,max_iter=10000)
    estimator.fit(x_train,y_train)
    #得出模型
    print("梯度下降权重系数:\n",estimator.coef_)
    print("梯度下降偏重:\n",estimator.intercept_)
    #模型评估
    print("梯度下降权重系数:\n", estimator.coef_)
    print("梯度下降偏重:\n", estimator.intercept_)
    # 模型评估
    y_predict = estimator.predict(x_test)
    print("梯度下降预测房价:\n", y_predict)
    error = mean_squared_error(y_test, y_predict)
    print("梯度下降均方误差:\n", error)
    return None

linear1()#正规方程
linear2()#梯度下降