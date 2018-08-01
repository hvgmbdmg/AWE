# -*- coding:utf-8 -*-
"""
This script is about file I/O, including load data, update file.
Data crawler is twstock.
"""
from twstock import Stock
import time
import csv
import re


'''
    This will create a new code file and load its data since 2005.
    Test version from 2017 to 201806
'''
def createNewfile( code ):
    '''
        1. Create a empty file only have title.
        2. call loadHistory function.
        That is all.
    '''
    title = ["Date", "Capacity", "Turnover", "Open", "High", "Low", "Close", "Change", "Transaction"]
    fileName = str(code) + ".csv"
    dataList = loadHistory( code, 2017, 1, 2018, 6 )
    with open( fileName, 'w+', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerow(title)
        w.writerows(dataList)
    print( "========================================================" )
    print( "=                 Create " , str(code) , " finish                 =" )
    print( "========================================================" )


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
            time.sleep(3)
        print( "========================================================" )
        print( "=                 Load  " , year , "  finish                 =" )
        print( "========================================================" )
    
    i = 1 if FinalYear>startYear else startMonth
    for month in range(i,FinalMonth+1):
        stock.fetch(FinalYear, month)
        for index in range(len(stock.data)):
            newItem = list(stock.data[index])
            newDate = newItem.pop(0)
            newItem.insert(0, newDate.strftime("%Y-%m-%d"))
            monthList.append(newItem)
        time.sleep(3)
    print( "========================================================" )
    print( "=                 Load  " , str(Code) , "  finish                 =" )
    print( "========================================================" )

    return monthList


def findLastDate( code ):
    lastDate = ''
    fileName = str(code) + '.csv'
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
    lastDateStr = findLastDate( code )
    # lastDate = lastDateStr.split('-')
    lastDate = re.split('-|/',lastDateStr)
    dataList = loadHistory( code, int(lastDate[0]), int(lastDate[1]), untilYear, untilMonth )

    isFind = False

    while ~isFind :
        item = dataList[0]
        if item[0]==lastDateStr :
            isFind = True
            # this shouldn't mask, just test
            del dataList[0]
            break
        del dataList[0]

    fileName = str(code) + ".csv"
    with open( fileName, 'a+', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(dataList)

# updateFile(2402, 2018, 8)
createNewfile(2330)
# updateFile(2330, 2018, 8)