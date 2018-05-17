#-*-coding:utf8-*-

import itertools
import datetime
import numpy as np

a = np.array(['a','b','c','d','e','f','g','h','i','j'])

pat_list = []
start = datetime.datetime.now()
for i in range(1,len(a)+1):
    print (i)
    pat_list.append(list(itertools.permutations(a,i)))

end = datetime.datetime.now()
print ((end-start).total_seconds())
