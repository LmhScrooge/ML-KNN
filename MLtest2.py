import numpy
import matplotlib.pyplot as plt
fh = open('datingText.txt')
arrLines = fh.readlines()
Linenumber = len(arrLines)
Mat = numpy.zeros((Linenumber,3))
classlabel = []
index = 0
#print(arrLines)
#print(Linenumber)
#print(Mat)
for lines in arrLines:
    line = lines.strip()
    list = line.split('\t')
    Mat[index] = list[0:3]
    index += 1
print(Mat)
ZeroMat = numpy.zeros(numpy.shape(Mat))
print(len(ZeroMat))