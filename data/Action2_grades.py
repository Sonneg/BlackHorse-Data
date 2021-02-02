# -*- coding: UTF-8 -*-

import numpy as np
from pandas import DataFrame

grades = {'姓名':['张飞','关羽','刘备','典韦','许褚'],'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}
df = DataFrame(grades)
print('成绩')
print(df,'\n')

# 计算语文成绩
avrg_Chinese = df['语文'].mean()
min_Chinese  = df['语文'].min()
max_Chinese  = df['语文'].max()
var_Chinese  = df['语文'].var()
std_Chinese  = df['语文'].std()
print('语文成绩统计')
print('avrg_Chinese :',avrg_Chinese ,'\n', 'min_Chinese :',min_Chinese ,'\n',\
      'max_Chinese :',max_Chinese ,'\n', 'var_Chinese :',var_Chinese ,'\n', 'std_Chinese :',std_Chinese)
print('\n')

# 计算数学成绩
avrg_Math = df['数学'].mean()
min_Math = df['数学'].min()
max_Math= df['数学'].max()
var_Math = df['数学'].var()
std_Math = df['数学'].std()
print('数学成绩统计')
print('avrg_Math:',avrg_Math,'\n', 'min_Math:',min_Math,'\n',\
      'max_Math:',max_Math,'\n', 'var_Math:',var_Math,'\n', 'std_Math:',std_Math)
print('\n')

# 计算英语成绩
avrg_English = df['英语'].mean()
min_English = df['英语'].min()
max_English = df['英语'].max()
var_English = df['英语'].var()
std_English = df['英语'].std()
print('英语成绩统计')
print('avrg_English:',avrg_English,'\n', 'min_English:',min_English,'\n',\
      'max_English:',max_English,'\n', 'var_English:',var_English,'\n', 'std_English:',std_English)
print('\n')

# 计算每人总成绩并排名
df['总成绩'] = df.iloc[:,1:].sum(axis=1)
#print(df, '\n')

df1 = df.sort_values('总成绩', ascending=False)
df1['排名'] = [1,2,3,4,5]
print('总成绩排名')
print(df1)




