# -*- coding:utf-8 -*-
import time
import csv
import re
import datetime


def read_daily_raw_data( year, month, day ):
    if month<10:
        month = '0'+str(month)
    if day<10:
        day = '0'+str(day)

    path = r'C:\Users\user\Desktop\RawPoint'
    fileName = '\Daily_'+str(year)+'_'+str(month)+'_'+str(day)+'.csv'
    thisDeadline = str(year)+str(month)+'     '
    nextDeadline = str(year)+str(int(month)+1)+'     '
    print(thisDeadline)
    print(nextDeadline)

    if month=='12':
        nextDeadline = str(year+1)+'01     '
    dataList = list()
    with open( path + fileName, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:

            if row[1]=='TX     ' and (row[2]==thisDeadline or row[2]==nextDeadline):
                if len(row)!=9:
                    print(len(row))
                dataList.append(row)
        print(len(dataList))

    save_path = r"C:\Users\user\Desktop\ResultPoint\TX"
    with open( save_path + fileName, 'w+', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(dataList)

    daytimeList = only_day_time_data(dataList)
    save_path = r"C:\Users\user\Desktop\ResultPoint\TX\daytime"
    with open( save_path + fileName, 'w+', newline='') as csvfile:
        w = csv.writer(csvfile)
        w.writerows(dataList)

    return dataList


def only_day_time_data( dataList ):
    dayStart = '084500'
    isDaytime = False
    while ~isDaytime :
        item = dataList[0]
        if item[3]==dayStart :
            isDaytime = True
            break
        del dataList[0]
    return dataList

def raw_to_minutes(minutes):


    return 

def raw_data_to_minutes_data(dataList):
    one_minutes     = raw_to_minutes(dataList, 1)
    five_minutes    = raw_to_minutes(dataList, 5)
    ten_minutes     = raw_to_minutes(dataList, 10)
    fifteen_minutes = raw_to_minutes(dataList, 15)
    twenty_minutes  = raw_to_minutes(dataList, 20)
    thirty_minutes  = raw_to_minutes(dataList, 30)
    sixty_minutes   = raw_to_minutes(dataList, 60)

    return one_minutes, five_minutes, ten_minutes, fifteen_minutes, twenty_minutes, thirty_minutes, sixty_minutes




read_daily_raw_data(2018,5,23)