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
    Test version from 2016 to 201806
'''
def createNewfile( code ):
    title = ["Date", "Capacity", "Turnover", "Open", "High", "Low", "Close", "Change", "Transaction"]
    fileName = str(code) + ".csv"
    dataList = loadHistory( code, 2016, 1, 2018, 6 )
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
    lastDateStr = findLastDate( code )
    lastDate = re.split('-|/',lastDateStr)
    dataList = loadHistory( code, int(lastDate[0]), int(lastDate[1]), untilYear, untilMonth )

    isFind = False
    while ~isFind :
        item = dataList[0]
        if item[0]==lastDateStr :
            isFind = True
            del dataList[0]
            break
        del dataList[0]

    fileName = str(code) + ".csv"
    with open( fileName, 'a+', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(dataList)


# updateFile(2402, 2018, 8)
import personal

for i in range(len(personal.attentionList)):
    code = personal.attentionList[i]
    createNewfile(code )
    updateFile(code , 2018, 8)
    time.sleep(4)

#createNewfile(2371 )
#updateFile(2371 , 2018, 8)