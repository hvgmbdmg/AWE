from twstock import Stock
import time

# load history data.
for x in range(6): # 0~6
    stock.fetch(2018, x)
    print(stock.data)
    time.sleep(5)


with open('2371.csv', newline='') as csvfile:
  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
  for row in rows:
    print(row)


f = open('2402.csv', 'w', newline='')
w = csv.writer(f)
w.writerows(stock.data)
# w.writerows(monthList)
f.close()


def loadHistory( Code ):
    stock = Stock(str(Code))
    monthList = list()
    for x in range(4,8): # 0~6
        stock.fetch(2018, x)
        # print(stock.data)
        for y in range(len(stock.data)):
            newItem = list(stock.data[y])
            newDate = newItem.pop(0)
            newItem.insert(0, newDate.strftime("%Y-%m-%d"))
            monthList.append(newItem)
        time.sleep(5)
    fileName = str(Code);



def openFileTest( fileName ):
    with open('fileName', newline='') as csvfile:
        # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)
        # 以迴圈輸出每一列
        for row in rows:
            print(row)
