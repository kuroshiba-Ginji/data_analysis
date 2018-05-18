#!/usr/bin/env python3
#-*-coding:utf8-*-

import itertools
import datetime
import numpy as np

a = np.array(['a','b','c','d','e','f','g','h','i','j'])


def nplist():
    start = datetime.datetime.now()
    pat_list = []
    for i in range(1,len(a)+1):
        list(itertools.permutations(a,i))

    end = datetime.datetime.now()
    print ("nplist: ", (end-start).total_seconds())

def allsubperms(a):
    for i in range(1,len(a)+1):
        for e in itertools.permutations(a,i):
            yield e

def npgen():
    start = datetime.datetime.now()
    pat_list = list(allsubperms(a))
    end = datetime.datetime.now()
    print ("npgen: ", (end-start).total_seconds())

def npnomat():
    start = datetime.datetime.now()
    for e in allsubperms(a):
        pass
    end = datetime.datetime.now()
    print ("npnomat: ", (end-start).total_seconds())

for i in range(1,7):
    nplist()
    npgen()
    npnomat()
