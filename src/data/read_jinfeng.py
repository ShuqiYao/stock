#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 11:51
# @Author  : Shuqi Yao

# 读取金风的历史股价
# 保存金风科技 A 股以及港股股票到/data 文件中

import tushare as ts
import pandas as pd
import numpy as np

# 获取备用连接
cons = ts.get_apis()

# jf_sz = ts.get_h_data('002202',start='2016-01-01',end='2018-06-30')
jf_sz = ts.bar('002202',conn=cons,start_date='2016-01-01',end_date='2018-06-30')
jf_sz.head(5)
jf_sz.to_csv('/Users/yaoshuqi/OneDrive/working/python/prac/stock/data/jf_sc.csv', encoding='utf-8')

jf_hk = ts.bar('02208',conn=cons,asset='X',start_date='2016-01-01',end_date='2018-06-30')

jf_hk.to_csv('/Users/yaoshuqi/OneDrive/working/python/prac/stock/data/jf_hk.csv',encoding='utf-8')