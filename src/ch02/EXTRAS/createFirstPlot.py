"""
Created on 2018-05-18

@author: Shiyipaisizuo
"""
from numpy import *
from src.ch02.EXTRAS import KNN
import matplotlib
import matplotlib.pyplot as plt
#解决matplotlib无法显示中文的问题
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

fig = plt.figure()
ax = fig.add_subplot(111)
datingDataMat,datingLabels = KNN.file2matrix('../datingTestSet.txt')
#ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
ax.axis([-2, 25, -0.2, 2.0])
plt.xlabel('花在玩电子游戏上的时间百分比')
plt.ylabel('每周消耗数升冰淇淋')
plt.show()
