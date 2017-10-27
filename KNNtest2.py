# -*- coding:UTF-8 -*-
import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import operator

#分类器计算结果
def classsify(inX,Mat,Labels,k):
    #返回Mat的行数
    rows = len(Mat)
    #构造一个和Mat行数一样多的样本数据
    example = np.tile(inX,(rows,1))
    #相减后平方
    sqex = (example - Mat)**2
    #按行相加
    sqnum = sqex.sum(axis=1)
    #开方
    sqlast = sqnum ** 0.5
    #设置空字典
    classdist = {}
    #按索引号排序
    sqsort = sqlast.argsort()
    for i in range(k):
        #获取第i个最小值的label
        vallabel = Labels[sqsort[i]]
        # 用get方法给计算每一个Label的频率
        # get(self,default).....self为获取名为self的value值，若没有value值则给value赋值default
        classdist[vallabel] = classdist.get(vallabel,0) + 1
        # python3中用items()替换python2中的iteritems()
        # key=operator.itemgetter(1)根据字典的值进行排序
        # key=operator.itemgetter(0)根据字典的键进行排序
        # reverse降序排序字典
    sortlastclass = sorted(classdist.items(),key=operator.itemgetter(1),reverse=True)
    #返回次数最多的类别
    return sortlastclass[0][0]

#文件数据处理函数
def filemat(filename):
    fh = open(filename)
    #所有内容按行存储
    arrlines = fh.readlines()
    #读取行数量
    linenumber = len(arrlines)
    #建立0矩阵
    Mat = np.zeros((linenumber,3))
    #存储标签
    classlabel = []
    index = 0
    for line in arrlines:
    #s.strip(rm)，当rm空时,默认删除空白符(包括'\n','\r','\t',' ')
        linearr = line.strip()
    # 使用s.split(str="",num=string,cout(str))将字符串根据'\t'分隔符进行切片。
        linelist = linearr.split('\t')
    #将linelist放进Mat矩阵中的每一行里面
        Mat[index] = linelist[0:3]
    #根据linlist的最后一个变量对矩阵的每一行打上标签,1代表不喜欢,2代表魅力一般,3代表极具魅力
        if linelist[-1] == 'didntLike':
            classlabel.append(1)
        if linelist[-1] == 'smallDoses':
            classlabel.append(2)
        if linelist[-1] == 'largeDoses':
            classlabel.append(3)
        index += 1
    return Mat,classlabel

def showdatas(Mat,Labels):
    #设置汉字格式
    font = FontProperties(fname = r"C:\Windows\Fonts\simhei.ttf",size=10)
    # 将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
    # 当nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域
    fig,axs = plt.subplots(nrows = 2,ncols = 2,sharex = False,sharey = False,figsize = (13,8))
    numberoflabels = len(Labels)
    Labelcolor = []
    for i in Labels:
        if i == 1:
            Labelcolor.append('black')
        if i == 2:
            Labelcolor.append('orange')
        if i == 3:
            Labelcolor.append('red')

    # 画出散点图,以datingDataMat矩阵的第一(飞行常客例程)、第二列(玩游戏)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][0].scatter(x=Mat[:,0],y=Mat[:,1],color=Labelcolor,s=15,alpha=0.5)
    # 设置标题,x轴label,y轴label
    axs0_title_text = axs[0][0].set_title(u'每年获得的飞行常客里程数与玩视频游戏所消耗时间占比',FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(u'每年获得的飞行常客里程数',FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'玩视频游戏所消耗时间占',FontProperties=font)
    plt.setp(axs0_title_text,size = 9,weight = 'bold',color = 'red')
    plt.setp(axs0_xlabel_text,size = 7,weight = 'bold',color = 'black')
    plt.setp(axs0_ylabel_text,size = 7,weight = 'bold',color = 'black')

    # 画出散点图,以datingDataMat矩阵的第一(飞行常客例程)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][1].scatter(x=Mat[:,0],y=Mat[:,2],color=Labelcolor,s=15,alpha=0.5)
    # 设置标题,x轴label,y轴label
    axs1_title_text = axs[0][1].set_title(u'每年获得的飞行常客里程数与每周消费的冰淇淋公斤数',FontProperties=font)
    axs1_xlabel_text = axs[0][1].set_xlabel(u'每年获得的飞行常客里程数',FontProperties=font)
    axs1_ylabel_text = axs[0][1].set_ylabel(u'每周消费的冰激淋公升数',FontProperties=font)
    plt.setp(axs1_title_text,size=9,weight= 'bold',color = 'red')
    plt.setp(axs1_xlabel_text,size = 7,weight = 'bold',color = 'black')
    plt.setp(axs1_ylabel_text,size = 7,weight = 'bold',color = 'black')

    # 画出散点图,以datingDataMat矩阵的第二(玩游戏)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[1][0].scatter(x=Mat[:,1],y=Mat[:,2],color=Labelcolor,s=15,alpha=0.5)
    # 设置标题,x轴label,y轴label
    axs2_title_text = axs[1][0].set_title(u'玩视频游戏所消耗时间占比与每周消费的冰激淋公升数',FontProperties=font)
    axs2_xlabel_text = axs[1][0].set_xlabel(u'玩视频游戏所消耗时间占',FontProperties=font)
    axs2_ylabel_text = axs[1][0].set_ylabel(u'每周消费的冰激淋公升数',FontProperties=font)
    plt.setp(axs2_title_text,size=9,weight= 'bold',color = 'red')
    plt.setp(axs2_xlabel_text,size = 7,weight = 'bold',color = 'black')
    plt.setp(axs2_ylabel_text,size = 7,weight = 'bold',color = 'black')

    #设置图例
    didntLike = mlines.Line2D([], [], color='black', marker='.',
                      markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                      markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                      markersize=6, label='largeDoses')
    # 添加图例
    axs[0][0].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[0][1].legend(handles=[didntLike, smallDoses, largeDoses])
    axs[1][0].legend(handles=[didntLike, smallDoses, largeDoses])
    # 显示图片
    plt.show()

def autonum(Mat):
    #获取最小值和最大值，max()和min()函数中的参数0代表行，1代表列
    minVals = Mat.min(0)
    maxvals = Mat.max(0)
    #最大值和最小值的范围
    rangevals = maxvals - minVals
    #建立一个初始化的零数组，大小和Mat一样
    ZeroMat = np.zeros(np.shape(Mat))
    #得到Mat的行数，有两种方法，一种len(),一种Mat.shape[i]，0为行数，1为列数
    rows = len(Mat)
    #rows = Mat.shape[0]
    #原始值减去最小值,np.tile(arr,(n,m))方法可以把以arr构成n * m的数组
    datamat = Mat - np.tile(minVals,(rows,1))
    #原始值除以范围，将数据归一化
    normdata = datamat / np.tile(rangevals,(rows,1))
    #返回归一化数据，最大值和最小值的范围，最小值
    return normdata,rangevals,minVals

#分类器测试函数
def classtest():
    #文件名
    filename = 'datingTextSet.txt'
    #解析文件，得到Mat和Labels
    Mat,Labels = filemat(filename)
    #归一化Mat,返回归一化后的矩阵,数据范围,数据最小值
    normMat,datarange,datamin = autonum(Mat)
    #设置测试样本数量百分比
    testpro = 0.1
    #获取矩阵行数
    m = normMat.shape[0]
    #测试样本数量
    testnum = int(m * testpro)
    #计算错误数量
    errornum = 0
    #对样本逐一进行测试，测试样本为前testnum个，训练集为testnum至m
    for i in range(testnum):
        #得到测试结果
        classsifyresult = classsify(normMat[i,:],normMat[testnum:m,:],Labels[testnum:m],4)
        #print("分类结果:%d\t真实类别:%d" % (classsifyresult, Labels[i]))
        if classsifyresult != Labels[i]:
            errornum += 1
    print("错误率：%f%%"%(errornum/testnum*100))

#输入样本数据得到分类结果
def classperson():
    #输出结果
    result = ['讨厌','有些喜欢','非常喜欢']
    #三维特征用户输入
    ffmiles = float(input("每年飞行里程数:"))
    precentTats = float(input("玩游戏所占时间百分比:"))
    icecream = float(input("每周消费冰淇淋公斤数:"))
    #打开的文件名
    filename = 'datingTextSet.txt'
    #打开并处理数据
    Mat,Labels = filemat(filename)
    #训练集归一化
    normdata,rangeval,minval = autonum(Mat)
    #测试数据矩阵化
    arr = np.array([ffmiles,precentTats,icecream])
    #测试数据归一化
    autodata = (arr - minval)/rangeval
    #返回分类结果
    classfierresult = classsify(autodata,normdata,Labels,3)
    print(result[classfierresult - 1])
if __name__ == "__main__":
    filename = 'datingTextSet.txt'
    """
    Mat,classlabel = filemat(filename)
    print(Mat)
    print(classlabel)
    showdatas(Mat,classlabel)
    """
    classperson()