
from twstock import Stock
from math import radians
import numpy as np     # installed with matplotlib
import matplotlib.pyplot as plt
import time
import csv



stock = Stock('2371')                             # 擷取台積電股價
ma_p = stock.moving_average(stock.price, 5)       # 計算五日均價
ma_c = stock.moving_average(stock.capacity, 5)    # 計算五日均量
ma_p_cont = stock.continuous(ma_p)                # 計算五日均價持續天數
ma_br = stock.ma_bias_ratio(5, 10)                # 計算五日、十日乖離值

print( stock.price )

# stock.fetch(2018, 1)
# print(stock.data)
 
# load history data.
for x in range(6):
    stock.fetch(2018, x)
    print(stock.data)
    time.sleep(5)


f = open('2371.csv', 'w')
w = csv.writer(f)
w.writerows(stock.data)
f.close()

# save path: C:\Users\albert_shen\AppData\Local\Programs\Python\Python37

"""
def main():
    x = np.arange(0, radians(1800), radians(12))
    plt.plot(x, np.cos(x), 'b')
    plt.show()

main()
"""