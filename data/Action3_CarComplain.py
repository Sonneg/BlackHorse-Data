# -*- coding: UTF-8 -*-

import numpy as np
import pandas as pd

#数据加载
df = pd.read_excel('./car_complain.xlsx')
# 拆分problem
df = df.drop(['problem'], axis=1).join(df.problem.str.get_dummies(','))

# 品牌投诉总数分析
# 合并重复值
df['brand'] = df['brand'].replace('一汽-大众','一汽大众')
# 以brand为基础对id列进行计数，返回列名为count
result1 = df.groupby(['brand'])['id'].agg(['count'])
# 更改列名
result1 = result1.rename(columns={'count':'Total'})
#print(result1)

# 定义问题标签
tags = df.columns[7:]
# 以brand为基础对tags数据进行求和处理
result2 = df.groupby(['brand'])[tags].agg('sum')
#print(result2)
# 将问题总数表和单个问题表合并
result2 = result1.merge(result2, left_index=True, right_index=True, how='left')
# 重置索引列
result2.reset_index(inplace = True)
# 对Total列从大到小排序
result_brand = result2.sort_values('Total', ascending=False)
print('品牌投诉总数分析')
print(result_brand)

print('---------------------------------------------------------------------------\n')


# 车型投诉总数分析
result3 = df.groupby(['car_model'])['id'].agg(['count'])
result3 = result3.rename(columns={'count':'Total'})
#print(result3)
result4 = df.groupby(['car_model'])[tags].agg('sum')
#print(result4)
result4 = result3.merge(result4, left_index=True, right_index=True, how='left')
result4.reset_index(inplace = True)
result_car_model = result4.sort_values('Total', ascending=False)
print('车型投诉总数分析')
print(result_car_model)


