# -*- coding: utf-8 -*-
import priceIndicator
import plotly
import plotly.plotly as py
import plotly.graph_objs as go 

from datetime import datetime


dataList = priceIndicator.readFile( 2330 )

#K, D, J = priceIndicator.KDJ( dataList, 9 )
#DIF, DEM, OSC = priceIndicator.MACD( dataList )#, quickN=12, slowN=26, demN=9 )


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



trace = go.Candlestick(x=Date,
                       open=Open,
                       high=High,
                       low=Low,
                       close=Close)


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


data = [trace]


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

yaxis=dict(
    autorange=True
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

'''
updatemenus = list([
    dict(active=-1,
         buttons=list([   
            dict(label = 'KD',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': '2330 KD'}]),
                          #,'annotations': high_annotations}]),
            dict(label = 'MACD',
                 method = 'update',
                 args = [{'visible': [False, False, True, True]},
                         {'title': '2330 MACD'}]),
                          #,'annotations': low_annotations}]),
            dict(label = 'Both',
                 method = 'update',
                 args = [{'visible': [True, True, True, True]},
                         {'title': '2330 KD & MACD'}]),
                          #,'annotations': high_annotations+low_annotations}]),
            dict(label = 'Reset',
                 method = 'update',
                 args = [{'visible': [True, True, False, False]},
                         {'title': '2330 Reset',
                          'annotations': []}])
        ]),
    )
])
'''

# if we need to look multi chart at same window, we should give our only width and height.
# Ex. dict(title='2330', width=1500, height=2000, showlegend=False, xaxis=xaxis , updatemenus=updatemenus)
layout = dict(title='2330',showlegend=False,
              xaxis=xaxis,yaxis=yaxis)# , updatemenus=updatemenus)

plotly.offline.plot({
    "data": data,
    "layout": layout
}, filename='2330.html'
 , auto_open=True)

