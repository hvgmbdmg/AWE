# -*- coding: utf-8 -*-
import priceIndicator
import plotly
import plotly.plotly as py
import plotly.graph_objs as go 

from datetime import datetime

#import pandas_datareader as web
#df = web.DataReader("aapl", 'yahoo',
#                    datetime(2015, 1, 1),
#                    datetime(2016, 7, 1))

# add one drop down, let user can choose stock code and load it's data
# dash example can do this, I think offline also can.
code = 3029

dataList = priceIndicator.readFile( code )

five_time   = priceIndicator.MA( dataList, 5 )
ten_time    = priceIndicator.MA( dataList, 10 )
twenty_time = priceIndicator.MA( dataList, 20 )

K, D, J = priceIndicator.KDJ( dataList, 9 )
DIF, DEM, OSC = priceIndicator.MACD( dataList )#, quickN=12, slowN=26, demN=9 )


Date     = list()
Capacity = list()
Open     = list()
High     = list()
Low      = list()
Close    = list()

for data in dataList:
    Date.append(data[0])
    Capacity.append(str(float(data[2])/1000))
    Open.append(data[3])
    High.append(data[4])
    Low.append(data[5])
    Close.append(data[6])

go_PRICE = go.Candlestick(x=Date,
                          open=Open,
                          high=High,
                          low=Low,
                          close=Close)

go_volume = go.Bar() # maybe

go_MA_5T  = go.Scatter(x=Date,
                       y=five_time,
                       name=str(code) + " 5")
go_MA_10T = go.Scatter()
go_MA_20T = go.Scatter()

go_KD_K = go.Scatter(
                x=Date,
                y=K,
                name=str(code) + " K",
                line=dict(color = '#17BECF'),
                opacity=0.8)

go_KD_D = go.Scatter(
                x=Date,
                y=D,
                name=str(code) + " D",
                line=dict(color = '#7F7F7F'),
                opacity=0.8)


go_MACD_DIF = go.Scatter(
                x=Date,
                y=DIF,
                name=str(code) + " DIF",
                line=dict(color = '#17BECF'),
                opacity=0.6)

go_MACD_DEM = go.Scatter(
                x=Date,
                y=DEM,
                name=str(code) + " DEM",
                line=dict(color='#7F7F7F'),
                opacity=0.6)


go_MACD_OSC = go.Bar() # maybe


'''
trace_high = go.Scatter(x=list(Date),
                        y=list(df.High),
                        name='High',
                        line=dict(color='#33CFA5'))

trace_high_avg = go.Scatter(x=list(df.index),
                            y=[df.High.mean()]*len(df.index),
                            name='High Average',
                            visible=False,
                            line=dict(color='#33CFA5', dash='dash'))

trace_low = go.Scatter(x=list(df.index),
                       y=list(df.Low),
                       name='Low',
                       line=dict(color='#F06A6A'))

trace_low_avg = go.Scatter(x=list(df.index),
                           y=[df.Low.mean()]*len(df.index),
                           name='Low Average',
                           visible=False,
                           line=dict(color='#F06A6A', dash='dash'))
'''


data = [go_KD_K, go_KD_D, go_MACD_DIF, go_MACD_DEM]


xaxis=dict(
    rangeselector=dict(
        buttons=list([
            dict(count=1,
                 label='2m',
                 step='month',
                 stepmode='backward'),
            dict(count=6,
                 label='6m',
                 step='month',
                 stepmode='backward'),
            dict(count=1,
                 label='1y',
                 step='year',
                 stepmode='backward'),
            dict(step='all')
            ])
        ),
    rangeslider=dict(
        visible = True
        ),
    type='date'
    
    )



'''
high_annotations=[dict(x='2016-03-01',
                       y=df.High.mean(),
                       xref='x', yref='y',
                       text='High Average:<br>'+str(df.High.mean()),
                       ax=0, ay=-40),
                  dict(x=df.High.idxmax(),
                       y=df.High.max(),
                       xref='x', yref='y',
                       text='High Max:<br>'+str(df.High.max()),
                       ax=0, ay=-40)]
low_annotations=[dict(x='2015-05-01',
                      y=df.Low.mean(),
                      xref='x', yref='y',
                      text='Low Average:<br>'+str(df.Low.mean()),
                      ax=0, ay=40),
                 dict(x=df.High.idxmin(),
                      y=df.Low.min(),
                      xref='x', yref='y',
                      text='Low Min:<br>'+str(df.Low.min()),
                      ax=0, ay=40)]
'''


updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'KD',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': str(code)+' KD'}]),
                          #,'annotations': high_annotations}]),
            dict(label = 'MACD',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                         {'title': str(code)+' MACD'}]),
                          #,'annotations': low_annotations}]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True, True, True, True]},
                         {'title': str(code)+' KD & MACD',
                          'annotations': []}])
        ]),
    )
])

# if we need to look multi chart at same window, we should give our only width and height.
# Ex. dict(title='2330', width=1500, height=2000, showlegend=False, xaxis=xaxis , updatemenus=updatemenus)
layout = dict(title=str(code),showlegend=False,
              xaxis=xaxis, updatemenus=updatemenus)

plotly.offline.plot({
    "data": data,
    "layout": layout
}, filename=str(code)+' KD and MACD.html'
 , auto_open=True)
