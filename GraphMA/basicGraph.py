# -*- coding: utf-8 -*-
import priceIndicator
import plotly
import plotly.graph_objs as go
import time
# import plotly.plotly as py
# import datetime
# import numpy as np



dataList = priceIndicator.readFile(2330)

K, D, J = priceIndicator.KDJ( dataList, 9 )

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



go_K = go.Scatter(
                x = Date,
                y = K,
                name = str(2330) + " K",
                line = dict(color = '#17BECF'),
                opacity = 0.8)

go_D= go.Scatter(
                x=Date,
                y=D,
                name = str(2330) + " D",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)


data = [go_K, go_D]


# https://plot.ly/python/reference/#layout-xaxis-rangeslider
# step ( enumerated : "month" | "year" | "day" | "hour" | "minute" | "second" | "all" )
layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all'),
                dict(count=15,
                     label='15min',
                     step='minute',
                     stepmode='backward'),
                dict(count=1,
                     label='Y',
                     step='year',
                     stepmode='backward')
            ])
        ),
        rangeslider=dict(
            visible = True
        ),
        type='date'
    )
)

plotly.offline.plot({
    "data": data,
    "layout": layout
}, filename='2330 KD Graph.html'
 , auto_open=False)


#fig = dict(data=data, layout=layout)
#py.iplot(fig, filename = "Time Series with Rangeslider")