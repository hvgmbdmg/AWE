# -*- coding:utf-8 -*-
"""
This script is about file I/O, including load data, update file.
Data crawler is twstock.
"""
from twstock import Stock
import time


'''
    This will create a new code file and load its data since 2005.
'''
def AddNewfile():
    '''
        1. Create a empty file only have title.
        2. call loadHistory function.
        That is all.
    '''
    return 


def loadHistory( Code, startYear, startMonth, FinalYear, FinalMonth ):
    stock = Stock(str(Code))
    monthList = list()
    for year in range( startYear, FinalYear ):
        for month in range( 1, 13 ):
            stock.fetch( year, month )

            for index in range(len(stock.data)):
                newItem = list(stock.data[index])
                newDate = newItem.pop(0)
                newItem.insert(0, newDate.strftime("%Y-%m-%d"))
                monthList.append(newItem)
            time.sleep(5)
        print( "========================================================" )
        print( "=                 Load   " , year , "   finish                 =" )
        print( "========================================================" )
    

    for month in range(1,FinalMonth+1):
        stock.fetch(FinalYear, month)
        for index in range(len(stock.data)):
            newItem = list(stock.data[index])
            newDate = newItem.pop(0)
            newItem.insert(0, newDate.strftime("%Y-%m-%d"))
            monthList.append(newItem)
        time.sleep(5)
    print( "========================================================" )
    print( "=                 Load   " , str(Code) , "   finish                 =" )
    print( "========================================================" )

    return monthList


def findLastDate( code ):
    fileName = str(code) + '.csv'
    lastDate = ""
    with open( fileName, 'r', newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            lastDate = row[0]
            # 2018-06-05
    print( "last date is: " + lastDate )
    return lastDate

def updateFile( code, untilYear, untilMonth ):
    '''
        1. Call findLastDate ... ok
        2. Call loadHistory ... ok
        3. write csv in a mode
    '''
    lastDate = findLastDate( code )
    lastDate = lastDate.split('-')

    dataList = loadHistory( code, int(lastDate[0]), int(lastDate[1]), untilYear, untilMonth )


    with open('fileName', 'a+',newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        # 以迴圈輸出每一列
        for row in rows:
            print(row)