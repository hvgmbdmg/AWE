# -*- coding:utf-8 -*-
"""
This script is about capacity indicator.
For Eexample one daily capacity lower or higher some number, I want to remind user.
"""

'''

'''
def CMA( dataList, period ):
    result = []
    nowPeriod = list()

    for item in dataList:
        nowPeriod.append(item)
        if len( nowPeriod ) < period:
            result.append(None)
            continue
        else :
            del nowPeriod[0]
        average = sum( l[1] for l in nowPeriod )/(period*1000)
        result.append(average)

    return result