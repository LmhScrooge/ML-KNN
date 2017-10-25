import numpy as np
import operator

"""
函数说明:kNN算法,分类器

Parameters:
    inX - 用于分类的数据(测试集)
    dataSet - 用于训练的数据(训练集)
    labes - 分类标签
    k - kNN算法参数,选择距离最小的k个点
Returns:
    sortedClassCount[0][0] - 分类结果

Modify:
    2017-07-13
"""

def CreatDataSet():
    group = np.array(
        [[1, 101],
         [5, 89],
         [108, 5],
         [115, 8]])
    labels = ['爱情','爱情','动作','动作']
    return group,labels
def classsify(inX,dataset,labels,k):
    # numpy函数shape[0]返回dataSet的行数
    datasetsize = dataset.shape[0]
    # 在列向量方向上重复inX共1次(横向)，行向量方向上重复inX共dataSetSize次(纵向)
    #diffMat的值为inX(本身为1,2的数组)变为4,2的数组，和group相减的值
    diffMat = np.tile(inX, (datasetsize, 1)) - dataset
    #平方
    sqdiffMat = diffMat**2
    #和
    sqdiffsum = sqdiffMat.sum(axis=1)
    #开方
    sqmath = sqdiffsum**0.5
    #索引号排序
    sqsort = sqmath.argsort()
    #设置空字典，记录每一个Labels出现的频率
    classdist = {}
    #计算每一个labels在前k出现的频率
    for i in range(k):
        #从小到大排序的索引号所对应的label
        vallabel = labels[sqsort[i]]
        #用get方法给计算每一个Label的频率
        #get(self,default).....self为获取名为self的value值，若没有value值则给value赋值default
        classdist[vallabel] = classdist.get(vallabel,0) + 1
        # python3中用items()替换python2中的iteritems()
        # key=operator.itemgetter(1)根据字典的值进行排序
        # key=operator.itemgetter(0)根据字典的键进行排序
        # reverse降序排序字典
    sortclassdist = sorted(classdist.items(),key=operator.itemgetter(1),reverse=True)
    return sortclassdist[0][0]

if __name__ == "__main__":
    group,labels = CreatDataSet()
    print(group)
    print(labels)
    test = [100,5]
    test_group = classsify(test,group,labels,3)
    print(test_group)