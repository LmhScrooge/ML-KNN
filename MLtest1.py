import numpy as np
import operator
import os
"""
group = np.array(
        [[1, 101],
         [5, 89],
         [108, 5],
         [115, 8]])
labels = ['爱情','爱情','动作','动作']
k = int(3)
test = [101,20]
group_size = group.shape[0]
diff = np.tile(test,(group_size,1)) - group
sqdiff = diff*diff
sqsum = sqdiff.sum(axis=1)
sqend = sqsum**0.5
sortdist = sqend.argsort()
print(sqend)
print(sortdist)
classcount = {}
for i in range(k):
    a = labels[sortdist[i]]
    classcount[a] = classcount.get(a,0)+1
sortclass = sorted(classcount.items(),key=operator.itemgetter(0),reverse=True)
print(sortclass)
"""
fh = open('datingText.txt','w')
fh.close()