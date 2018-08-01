
from twstock import Stock
from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
import time
import csv

stock = Stock('2371')                             # 擷取股價
ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值


def readFile( code ):
    fileName = str(code) + '.csv'
    dataList = list()
    with open(fileName, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            dataList.append(row)
        del dataList[0]
    return dataList

# hightLevel, mediumLevel, lowLevel = findThereLevel(low, high)
def findThereLevel(low, high):
    parameter = 1.382;
    hightLevel  = low + (high-low)*parameter
    mediumLevel = (high+low)/2
    lowLevel    = high - (high-low)*parameter
    return hightLevel, mediumLevel, lowLevel


def listMinusList( a, b ):
    len = min( len(a), len(b) )
    result = []

    for i in range(len):
        result.append(a[i]-b[i])
    return result;


def MA( dataList, period ):
    result = []
    nowPeriod = list()

    for item in dataList:
        nowPeriod.append(item)
        if len( nowPeriod ) < period:
            continue
        else :
            del nowPeriod[0]
        average = sum( l[4] for l in nowPeriod )/period
        result.append(average)

    return result


'''
dataList = (['date', 'capacity', 'turnover', 'open','high', 'low', 'close', 'change', 'transaction'])
I think J is not always equal 3D - 2K
Maybe we can use K-D or 3K-2D
'''
def KDJ( dataList, period ):
    K, D, J = [], [], []
    last_k, last_d = None, None
    nowPeriod = list()
    for item in dataList:
        nowPeriod.append(item)
        if len( nowPeriod ) < period:
            continue
        else :
            del nowPeriod[0]

        if last_k is None or last_d is None:
            last_k = 50
            last_d = 50

        high  = max(l[4] for l in nowPeriod)
        low   = min(l[5] for l in nowPeriod)
        close = item[6]

        RSV = (close-low)/(high-low) * 100
        k = (2 / 3) * last_k + (1 / 3) * RSV
        d = (2 / 3) * last_d + (1 / 3) * k
        j = 3 * d - 2 * k

        K.append(k)
        D.append(d)
        J.append(j)

        last_k, last_d = k, d

    return K,D,J


'''
    exponential moving average
    choose close price
    n = 12/26 in macd
'''
def EMA( dataList, n ):
    EMA = []
    lastEMA = dataList[0][6]

    for item in dataList:
        newEMA = (2*item[6] + lastEMA*(n-1))/(n+1)
        lastEMA = newEMA
        EMA.append( newEMA )

    return EMA


'''
    Moving Average Convergence / Divergence, MACD
    OSC is a bar.
'''
def MACD( dataList, quickN=12, slowN=26, demN=9 ):
    quickEMA = EMA( dataList, quickN )
    slowEMA  = EMA( dataList, slowN )
    DIF = listMinusList( quickEMA, slowEMA )
    DEM = EMA( dataList, demN )
    OSC = listMinusList( DIF, DEM )

    return DIF, DEM, OSC


'''
def moving_average(self, data, days):
        result = []
        data = data[:]
        for _ in range(len(data) - days + 1):
            result.append(round(sum(data[-days:]) / days, 2))
            data.pop()
        return result[::-1]
'''


# datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# '2011-11-03 18:21:26'

# Absolute path
# with open(r'C:\...\...\...\2371.csv', newline='') as csvfile:
