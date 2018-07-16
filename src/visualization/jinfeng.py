#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/16 14:22
# @Author  : Shuqi Yao

import pandas as pd
import numpy as np
import matplotlib as plt
from dateutil import parser



jf_sz = pd.read_csv('/Users/yaoshuqi/OneDrive/working/python/prac/stock/data/jf_sc.csv')
jf_hk = pd.read_csv('/Users/yaoshuqi/OneDrive/working/python/prac/stock/data/jf_hk.csv')
# 把日期列转为日期格式，创建时序数据
jf_sz['datetime'] = jf_sz.datetime.apply(parser.parse)
jf_sz = jf_sz.set_index('datetime')