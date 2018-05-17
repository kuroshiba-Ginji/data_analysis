#-*-coding:utf8-*-

from sympy.utilities.iterables import multiset_permutations
import datetime
import numpy as np

a = np.array(['a','b','c','d','e','f','g','h','i','j'])

pat_list = []
start = datetime.datetime.now()
for i in range(1,len(a)+1):
    print (i)
    for p in multiset_permutations(a,i):
        pat_list.append(p)

end = datetime.datetime.now()
print ((end-start).total_seconds())
