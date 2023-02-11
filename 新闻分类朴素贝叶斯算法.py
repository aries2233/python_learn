from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def news_demo():
    #获取数据
    news=fetch_20newsgroups(subset="all")
    #划分数据值
    x_train,x_test,y_train,y_test=train_test_split(news.data,news.target)
    #特征工程
    transfer=TfidfVectorizer()
    x_train=transfer.fit_transform(x_train)
    x_test=transfer.transform(x_test)
    #朴素贝叶斯算法
    estimator=MultinomialNB()
    estimator.fit(x_train,y_train)
    #模型评估
    #法1 对比真实值和预测值
    y_predict = estimator.predict(x_test)
    print("y_predict:\n",y_predict)
    print("直接比对真实值和预测值：\n",y_test == y_predict)
    #法2 计算准确率
    score = estimator.score(x_test,y_test)
    print("准确率：\n",score)
    return None

news_demo()