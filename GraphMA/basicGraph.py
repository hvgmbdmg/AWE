# -*- coding: utf-8 -*-
import priceIndicator
import plotly
import plotly.graph_objs as go
# import plotly.plotly as py
# import datetime
# import numpy as np


dataList = priceIndicator.readFile(2330)

Date  = list()
Open  = list()
High  = list()
Low   = list()
Close = list()

for data in dataList:
    Date.append(data[0])
    Open.append(data[3])
    High.append(data[4])
    Low.append(data[5])
    Close.append(data[6])


plotly.offline.plot({
    "data": [go.Scatter(x=Date, y=Close)],
    "layout": go.Layout(title="hello plotly")
}, auto_open=True)
