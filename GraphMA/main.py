import aboutFile
import priceIndicator
import personal
import datetime

def dailyUpdate():
    now = datetime.datetime.now()
    for index in range(0, len(personal.attentionList)):
        aboutFile.updateFile( personal.attentionList[index], now.year, now.month )

def addNewStock( code ):
    now = datetime.datetime.now()
    personal.attentionList.append(code)
    personal.attentionList.sort()
    aboutFile.createNewfile(code)
    aboutFile.updateFile( code, now.year, now.month )

def dailyRemind():
    now = datetime.datetime.now()
    for index in range(0, len(personal.attentionList)):
        aboutFile
        aboutFile.updateFile( personal.attentionList[index], now.year, now.month )
    return ;

def normalRenewIndicator(  ):
    return 