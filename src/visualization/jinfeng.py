#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 14:22
# @Author  : Shuqi Yao

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser



jf_sz = pd.read_csv('data/jf_sc.csv',parse_dates=['datetime'],index_col=0,date_parser=parser.parse)
jf_hk = pd.read_csv('data/jf_hk.csv',parse_dates=['datetime'],index_col=0,date_parser=parser.parse)
# 把日期列转为日期格式，创建时序数据
# jf_sz['datetime'] = jf_sz.datetime.apply(parser.parse)
# jf_sz = jf_sz.set_index('datetime')

#提取出深圳的收盘价
close_sz = jf_sz['close']
close_hk = jf_hk['close']
#画图

# close_sz.plot()
plt.show(close_sz.plot())
plt.show(close_hk.plot())

plot_data = pd.concat([close_sz,close_hk],axis=1)
plot_data.columns = ['close_sz','close_hk']
plt.show(plot_data.plot())







#简单收益

simple_rate = (close_sz-close_sz.shift(1))/close_sz.shift(1)

simple_rate_sz =simple_rate.dropna()

simple_rate_2 = (close_hk-close_hk.shift(1))/close_hk.shift(1)

simple_rate_hk = simple_rate_2.dropna()

simple_rate_plot = pd.concat([simple_rate_sz,simple_rate_hk],axis=1)
simple_rate_plot.columns = ['sz_rate','hk_rate']

simple_rate_plot.plot()


#compare if two curves have any differences

# maybe we can try to use some