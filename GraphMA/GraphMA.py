
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


def openFileTest( fileName ):
    with open('fileName', newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        # 以迴圈輸出每一列
        for row in rows:
            print(row)

# print(stock.data)

# hightLevel, mediumLevel, lowLevel = findThereLevel(low, high)
def findThereLevel(low, high):
    parameter = 1.382;
    hightLevel  = low + (high-low)*parameter
    mediumLevel = (high+low)/2
    lowLevel    = high - (high-low)*parameter
    return hightLevel, mediumLevel, lowLevel


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

StockNo = 2371;
openFileTest( str(StockNo) + '.csv' )

with open('2371.csv', newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    print(row)


# save path: C:\Users\albert_shen\AppData\Local\Programs\Python\Python37
