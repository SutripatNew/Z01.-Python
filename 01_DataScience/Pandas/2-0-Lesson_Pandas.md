# 1. Series

## 1.1 Series (List & Tuple)

``` python
import pandas as pd
data_ls = [10,20,'kong',15.05,'มะละกอ']     #list
data_tp = (10,20,'kong',15.05,'มะละกอ')     #tuple

ps_ls = pd.Series(data_ls)      # ps = pandas series
ps_tp = pd.Series(data_tp)

# consist index and value
print(ps_ls)    
print("=============================================")
print(ps_tp)
```
<details>
<summary> output </summary>

``` python
# 0        10
# 1        20
# 2      kong
# 3     15.05
# 4    มะละกอ
# dtype: object
# =============================================
# 0        10
# 1        20
# 2      kong
# 3     15.05
# 4    มะละกอ
# dtype: object
```
</details>


## 1.2 Series (Numpy)

``` python
import pandas as pd
import numpy as np
ndata = np.array([10,20,'kong',15.05,'มะละกอ'])
ps_arr = pd.Series(ndata)

print(ps_arr)
```
<details>
<summary> output </summary>

``` python
# 0        10
# 1        20
# 2      kong
# 3     15.05
# 4    มะละกอ
# dtype: object
```
</details>


## 1.3 Series (Indicate index)

``` python
import pandas as pd
items = ['มะม่วง','กล้วย','องุ่น']
idx = [50,20,30]

ps = pd.Series(items, index=idx)
print(ps)
```

<details>
<summary> Output </summary>

``` python
# 50    มะม่วง
# 20     กล้วย
# 30     องุ่น
# dtype: object
```
</details>


## 1.4 Series (Dictionary)

``` python
import pandas as pd
color = {"green":"เขียว", "red":"แดง", "orange":"ส้ม", "yellow":"เหลือง"}
age = {"John":50,"Somchai":25,"Somsak":40}

ps1 = pd.Series(color)
ps2 = pd.Series(age)

print(ps1)
print("=============================================")
print(ps2)
```

<details>
<summary> Output </summary>

``` python
# green      เขียว
# red          แดง
# orange       ส้ม
# yellow    เหลือง
# dtype: object
# =============================================
# John       50
# Somchai    25
# Somsak     40
# dtype: int64
```
</details>

## 1.5 Access to data in Series (refer to index)

``` python
import pandas as pd
data = [10,20,30,40]

a = pd.Series(data)
print(a[1])         # index 1 : 20
```
<details>
<summary> Output </summary>

``` python
# 20
```
</details>


``` python
import pandas as pd
color = {"red":"แดง","yellow":"เหลือง","pink":"ชมพู"}

b = pd.Series(color)
print(b["yellow"])         # key yellow : เหลือง
```
<details>
<summary> Output </summary>

``` python
# เหลือง
```
</details>


# 2. DataFrame

## 2.1 DataFrame (List & Tuple)

``` python
import pandas as pd
datas1 = [10,20,30,40,50]       #list
datas2 = (59,60,25,32)          #tuple           
df1 = pd.DataFrame(datas1, columns=['age']) #columns header
df2 = pd.DataFrame(datas2)

display(df1)
print("=============================================")
display(df2)
```

<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

|  | age |
|-------|-----|
| 0     | 10  |
| 1     | 20  |
| 2     | 30  |
| 3     | 40  |
| 4     | 50  |

=============================================

||0|
|-|-|
|0|	59|
|1|	60|
|2|	25|
|3|	32|
</div>
</details>


## 2.2 DataFrame (List n dims -> List in List)

``` python
# input data row (transaction) form
# output data row (transaction) form
import pandas as pd
datas = [ ['คีย์บอร์ด','IT',4000], ['ตุ๊กตา','ของเล่น',500], ['เมาส์','IT',300] ]

df = pd.DataFrame(datas, columns=['ชื่อสินค้า', 'หมวดหมู่', 'ราคา'])
display(df)
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

| index | ชื่อสินค้า | หมวดหมู่ | ราคา |
|-------|-----------|----------|------|
| 0     | คีย์บอร์ด | IT       | 4000 |
| 1     | ตุ๊กตา    | ของเล่น  | 500  |
| 2     | เมาส์     | IT       | 300  |
</div>
</details>


## 2.3 DataFrame (List n dims -> zip)

``` python
# input data row (transaction) form
# output data column form
import pandas as pd
product1 = ['คีย์บอร์ด','ตุ๊กตา','เมาส์']
product2 = ['IT','ของเล่น','IT']
product3 = [4000,500,300]

datas = list(zip(product1,product2,product3))

df = pd.DataFrame(datas, columns=['ชื่อสินค้า', 'หมวดหมู่', 'ราคา'])
display(df)
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

| index | ชื่อสินค้า | หมวดหมู่ | ราคา |
|-------|-----------|----------|------|
| 0     | คีย์บอร์ด | IT       | 4000 |
| 1     | ตุ๊กตา    | ของเล่น  | 500  |
| 2     | เมาส์     | IT       | 300  |
<div>
</details>


## 2.4 DataFrame (Dictionary - Dic in List)

``` python
# input data row (transaction) form
# output data row (transaction) form
import pandas as pd
products = [{'Name':'คีย์บอร์ด', 'Category':'อุปกรณ์คอม', 'Price':500},
            {'Name':'เมาส์', 'Category':'อุปกรณ์คอม', 'Price':300},
            {'Name':'ตุ๊กตา', 'Category':'ของเล่น', 'Price':700}]

df = pd.DataFrame(products)
display(df)
print("=============================================")

df2 = df.set_index(["Name"])    # set index (once times)
display(df2)
# if you want to change permanent for df -> df.set_index(["Name"], inplace = True)
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

|  | Name      | Category    | Price |
|-------|-----------|-------------|------:|
| 0     | คีย์บอร์ด | อุปกรณ์คอม |   500 |
| 1     | เมาส์     | อุปกรณ์คอม |   300 |
| 2     | ตุ๊กตา    | ของเล่น    |   700 |

=============================================

| Name      | Category    | Price |
|-----------|-------------|------:|
| คีย์บอร์ด | อุปกรณ์คอม |   500 |
| เมาส์     | อุปกรณ์คอม |   300 |
| ตุ๊กตา    | ของเล่น    |   700 |
</div>
</details>


## 2.5 DataFrame (Series)

``` python
# input data column form
# output data column form

import pandas as pd
# product data
name = ["คีย์บอร์ด","เมาส์","ตุ๊กตา"]
category = ['อุปกรณ์คอม','อุปกรณ์คอม','ของเล่น']
price = [500, 300, 700]

# series
name_series = pd.Series(name)
category_series = pd.Series(category)
price_series = pd.Series(price)

frame = {"ชื่อสินค้า": name_series,"หมวดหมู่" : category_series,"ราคา" : price_series}

df = pd.DataFrame(frame)
display(df)
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

|  | ชื่อสินค้า | หมวดหมู่ | ราคา |
|-------|-----------|-----------|------:|
| 0     | คีย์บอร์ด | อุปกรณ์คอม |   500 |
| 1     | เมาส์     | อุปกรณ์คอม |   300 |
| 2     | ตุ๊กตา    | ของเล่น    |   700 |
</div>
</details>


## 2.6 DataFrame for file (csv)
### 2.6.1 Export to csv
Attribute <br>
- header : (Default:True)
- index : (Default:True)

``` python
# input data column form
# output data column form

import pandas as pd
# product data
name = ["คีย์บอร์ด","เมาส์","ตุ๊กตา"]
category = ['อุปกรณ์คอม','อุปกรณ์คอม','ของเล่น']
price = [500, 300, 700]

# series
name_series = pd.Series(name)
category_series = pd.Series(category)
price_series = pd.Series(price)

frame = {"ชื่อสินค้า": name_series,"หมวดหมู่" : category_series,"ราคา" : price_series}

df = pd.DataFrame(frame)
display(df)

df.to_csv(r'ExportFile\products.csv', index=False)
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

|  | ชื่อสินค้า | หมวดหมู่     | ราคา |
|-------|-----------|--------------|------:|
| 0     | คีย์บอร์ด | อุปกรณ์คอม |   500 |
| 1     | เมาส์     | อุปกรณ์คอม |   300 |
| 2     | ตุ๊กตา    | ของเล่น     |   700 |
</div>
</details>

### 2.6.2 Read file from csv

parameter <br>

- `encoding='utf-8'`
- `usecols = [...] `      -> <span style="color:red;">use for select some column(s)</span>
- `index_col = "..."`     -> <span style="color:red;">set index from selected</span>
- `names = "..."`        -> <span style="color:red;">indicate header name : (DataFrame use: columns=[...])</span>

``` python
import pandas as pd

file = pd.read_csv(r'ExportFile\products.csv', encoding='utf-8')
display(file)
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

|  | ชื่อสินค้า | หมวดหมู่     | ราคา |
|-------|-----------|--------------|------:|
| 0     | คีย์บอร์ด | อุปกรณ์คอม |   500 |
| 1     | เมาส์     | อุปกรณ์คอม |   300 |
| 2     | ตุ๊กตา    | ของเล่น     |   700 |
</div>
</details>

``` python
# usecols
# index_col
import pandas as pd

file = pd.read_csv(r'ExportFile\products.csv', encoding='utf-8', usecols=['ชื่อสินค้า', 'ราคา'])
display(file)
print("=============================================")
file = pd.read_csv(r'ExportFile\products.csv', encoding='utf-8', usecols=['ชื่อสินค้า', 'ราคา'], index_col='ชื่อสินค้า')
display(file)
# index_col='ชื่อสินค้า' == file.set_index('ชื่อสินค้า')
```
<details>
<summary> Output </summary>
<div style="margin-left:1em; margin-top:1em">

|  | ชื่อสินค้า | ราคา |
|-------|-----------|------:|
| 0     | คีย์บอร์ด |   500 |
| 1     | เมาส์     |   300 |
| 2     | ตุ๊กตา    |   700 |

=============================================

|  | ราคา |
|-----------|------:|
|ชื่อสินค้า| |
| คีย์บอร์ด |   500 |
| เมาส์     |   300 |
| ตุ๊กตา    |   700 |
</div>
</details>

``` python
# names
file = pd.read_csv(r'ExportFile\products.csv', encoding='utf-8', names=['Name', 'Cate', 'Price'])
display(file)

# names=['Name', 'Cate', 'Price'] == columns = ['Name', 'Cate', 'Price']

# datas1 = [10,20,30,40,50]
# df1 = pd.DataFrame(datas1, columns=['age'])
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

| | Name      | Cate        | Price |
|-------|-----------|-------------|------:|
| 1     | คีย์บอร์ด | อุปกรณ์คอม |   500 |
| 2     | เมาส์     | อุปกรณ์คอม |   300 |
| 3     | ตุ๊กตา    | ของเล่น    |   700 |
</div>
</details>


## 2.7 DataFrame for file (Excel)
- `pip install xlrd`

``` python
import pandas as pd

df = pd.read_excel(r"ExportFile\dataupdate.xlsx",'weather')     # indicate sheets = 'weather'ExportFile
display(df.head(5))
print("=============================================")
df2 = pd.read_excel(r"ExportFile\dataupdate.xlsx",'weather', index_col='Day')
# df2 = pd.read_excel(r"ExportFile\dataupdate.xlsx",'weather')
# df2.set_index('Day', inplace=True)
display(df2.head(5))
```
<details>
<summary> output </summary>

<div style="margin-left:1em; margin-top:1em">

| | Day        | Temperature | WindSpeed | Event   |
|-------|------------|------------:|----------:|---------|
| 0     | 2020-12-01 |          30 |         9 | แดดร้อน |
| 1     | 2020-12-02 |          28 |         8 | เมฆมาก  |
| 2     | 2020-12-03 |          27 |         4 | ฝนตก    |
| 3     | 2020-12-04 |          19 |         3 | แดดร้อน |
| 4     | 2020-12-05 |          20 |         5 | เมฆมาก  |

=============================================

|         | Temperature | WindSpeed | Event   |
|------------|------------:|----------:|---------|
| Day        |  |  |    |
| 2020-12-01 |          30 |         9 | แดดร้อน |
| 2020-12-02 |          28 |         8 | เมฆมาก  |
| 2020-12-03 |          27 |         4 | ฝนตก    |
| 2020-12-04 |          19 |         3 | แดดร้อน |
| 2020-12-05 |          20 |         5 | เมฆมาก  |
</div>
</details>


## 2.8 Verify data in DataFrame
<pre>
- head()        => <span style="color:red;">read the first 5 rows of data.</span>
- head(n)       => <span style="color:red;">read the first n rows of data.</span>
- tail()        => <span style="color:red;">read the last 5 rows of data.</span>
- tail(n)       => <span style="color:red;">read the last n rows of data.</span>
- sample(n)     => <span style="color:red;">sample n rows of data</span>
- describe(n)   => <span style="color:red;">statistic such as min-max mean etc.</span>
- shape         => <span style="color:red;">count rows/cols such as (20,4) = 20 rows / 4 cols</span>
- columns       => <span style="color:red;">Check what columns are present</span>
- values        => <span style="color:red;">read data array form</span>
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx','weather')
print(f"data have {df.shape[0]} rows and {df.shape[1]} cols => {df.shape}")
print("=============================================")
display(df.head(3))
print("=============================================")
display(df.describe())
```
<details>
<summary> Output </summary>

<p style="margin-left:1em; margin-top:1em"> data have 30 rows and 4 cols => (30, 4) </p>
<p style="margin-left:1em; margin-top:1em"> ============================================= </p>

<div style="margin-left:1em; margin-top:1em">

|  | Day        | Temperature | WindSpeed | Event   |
|-------|------------|------------:|----------:|---------|
| 0     | 2020-12-01 |          30 |         9 | แดดร้อน |
| 1     | 2020-12-02 |          28 |         8 | เมฆมาก  |
| 2     | 2020-12-03 |          27 |         4 | ฝนตก    |

|        | Day                 | Temperature | WindSpeed |
|--------|---------------------|------------:|----------:|
| count  | 30                  |   30.000000 | 30.000000 |
| mean   | 2020-12-15 12:00:00 |   27.433333 |  5.066667 |
| min    | 2020-12-01 00:00:00 |   17.000000 |  1.000000 |
| 25%    | 2020-12-08 06:00:00 |   25.000000 |  4.000000 |
| 50%    | 2020-12-15 12:00:00 |   28.000000 |  5.000000 |
| 75%    | 2020-12-22 18:00:00 |   30.000000 |  6.750000 |
| max    | 2020-12-30 00:00:00 |   38.000000 |  9.000000 |
| std    | NaN                 |    5.237026 |  2.288402 |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx','weather')
display(df.columns)
print("=============================================")
display(df.values)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` bash
Index(['Day', 'Temperature', 'WindSpeed', 'Event'], dtype='object') 
=============================================
array([[Timestamp('2020-12-01 00:00:00'), 30, 9, 'แดดร้อน'],
       [Timestamp('2020-12-02 00:00:00'), 28, 8, 'เมฆมาก'],
       [Timestamp('2020-12-03 00:00:00'), 27, 4, 'ฝนตก'],
       [Timestamp('2020-12-04 00:00:00'), 19, 3, 'แดดร้อน'],
       [Timestamp('2020-12-05 00:00:00'), 20, 5, 'เมฆมาก'],
       [Timestamp('2020-12-06 00:00:00'), 25, 6, 'ฝนตก'],
       [Timestamp('2020-12-07 00:00:00'), 36, 4, 'ฝนตก'],
       [Timestamp('2020-12-08 00:00:00'), 28, 6, 'ฝนตก'],
       [Timestamp('2020-12-09 00:00:00'), 17, 5, 'เมฆมาก'],
       [Timestamp('2020-12-10 00:00:00'), 24, 6, 'แดดร้อน'],
       [Timestamp('2020-12-11 00:00:00'), 26, 4, 'ฝนตก'],
       [Timestamp('2020-12-12 00:00:00'), 27, 9, 'แดดร้อน'],
       [Timestamp('2020-12-13 00:00:00'), 30, 2, 'แดดร้อน'],
       [Timestamp('2020-12-14 00:00:00'), 31, 5, 'เมฆมาก'],
       [Timestamp('2020-12-15 00:00:00'), 28, 4, 'แดดร้อน'],
       [Timestamp('2020-12-16 00:00:00'), 27, 7, 'แดดร้อน'],
       [Timestamp('2020-12-17 00:00:00'), 20, 8, 'ฝนตก'],
       [Timestamp('2020-12-18 00:00:00'), 18, 5, 'ฝนตก'],
       [Timestamp('2020-12-19 00:00:00'), 25, 7, 'แดดร้อน'],
       [Timestamp('2020-12-20 00:00:00'), 28, 4, 'เมฆมาก'],
       [Timestamp('2020-12-21 00:00:00'), 25, 5, 'เมฆมาก'],
       [Timestamp('2020-12-22 00:00:00'), 38, 2, 'เมฆมาก'],
       [Timestamp('2020-12-23 00:00:00'), 34, 3, 'ฝนตก'],
       [Timestamp('2020-12-24 00:00:00'), 29, 4, 'ฝนตก'],
       [Timestamp('2020-12-25 00:00:00'), 34, 5, 'แดดร้อน'],
       [Timestamp('2020-12-26 00:00:00'), 25, 8, 'ฝนตก'],
       [Timestamp('2020-12-27 00:00:00'), 28, 9, 'เมฆมาก'],
       [Timestamp('2020-12-28 00:00:00'), 30, 2, 'เมฆมาก'],
       [Timestamp('2020-12-29 00:00:00'), 31, 1, 'ฝนตก'],
       [Timestamp('2020-12-30 00:00:00'), 35, 2, 'ฝนตก']], dtype=object)
```
</div>
</details>


## 2.9 Statistic for DataFrame
<pre>
- mean()
- max()
- min()
- count()
- std()
- sum()
- astype('...')         => <span style="color:red;">Change data type</span>
- dtypes
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'score', index_col='Name')
print(f'mean : {df.Score.mean()}')
print(f'max : {df.Score.max()}')
print(f'min : {df.Score.min()}')
print(f'count : {df.Score.count()}')
print(f'std : {df.Score.std()}')
print(f'sum : {df.Score.sum()}')
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# mean : 72.44444444444444
# max : 95
# min : 45
# count : 9
# std : 17.95209675157133
# sum : 652
```
</div>
</details>

``` python
df.dtypes
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Score      int64
# Age        int64
# Gender    object
# Grade     object
# dtype: object
```
</div>
</details>

``` python
# Change data type with .astype()
df.Grade = df.Grade.astype('category')
df.dtypes
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Score        int64
# Age          int64
# Gender      object
# Grade     category
# dtype: object
```
</div>
</details>


## 2.10 Selected columns
<b>Columns</b>
- df.<span style="color:brown;">columnsName</span> <br>
- df[<span style="color:brown;">columnsName</span>] <br>

<b>Range</b>
- df.<span style="color:brown;">columnsName</span>.[...]

``` python
# df.<columnsName>
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col="Day")
print(df.Temperature)
# print(df['Temperature'])
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Day
# 2020-12-01    30
# 2020-12-02    28
# 2020-12-03    27
# 2020-12-04    19
# 2020-12-05    20
# 2020-12-06    25
# 2020-12-07    36
# 2020-12-08    28
# 2020-12-09    17
# 2020-12-10    24
# 2020-12-11    26
# 2020-12-12    27
# 2020-12-13    30
# 2020-12-14    31
# 2020-12-15    28
# 2020-12-16    27
# 2020-12-17    20
# 2020-12-18    18
# 2020-12-19    25
# 2020-12-20    28
# 2020-12-21    25
# 2020-12-22    38
# 2020-12-23    34
# 2020-12-24    29
# ...
# 2020-12-28    30
# 2020-12-29    31
# 2020-12-30    35
# Name: Temperature, dtype: int64
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```
</div>
</details>

``` python
# df.<columnsName>.[...]
import pandas as pd
df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col="Day")
display(df[['Temperature','Event']][1:6])      # index = 1-5 => row = 2-6
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">


|         | Temperature | Event   |
|------------|------------:|---------|
| Day        |  |    |
| 2020-12-02 |          28 | เมฆมาก  |
| 2020-12-03 |          27 | ฝนตก    |
| 2020-12-04 |          19 | แดดร้อน |
| 2020-12-05 |          20 | เมฆมาก  |
| 2020-12-06 |          25 | ฝนตก    |
</div>
</details>


## 2.11 Selected rows

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col="Day")
display(df[1:4])        # index = 1-3 => row = 2-4
print("=============================================")
display(df[1:4]['WindSpeed'])
# display(df['WindSpeed'][1:4])
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Temperature | WindSpeed | Event   |
|------------|------------:|----------:|---------|
| Day        |  |  |    |
| 2020-12-02 |          28 |         8 | เมฆมาก  |
| 2020-12-03 |          27 |         4 | ฝนตก    |
| 2020-12-04 |          19 |         3 | แดดร้อน |

=============================================

``` python
Day
2020-12-02    8
2020-12-03    4
2020-12-04    3
Name: WindSpeed, dtype: int64
```
</div>
</details>

``` python
# df.loc[ช่วงแถว,ช่วงหลัก]
# df.loc[[แถว], [หลัก]]
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col="Day")
df.loc['2020-12-02':'2020-12-07', ['Event','Temperature']]
# df.loc[['2020-12-02','2020-12-03','2020-12-07','2020-12-04','2020-12-05','2020-12-06','2020-12-07'], ['Event','Temperature']]
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Event   | Temperature |
|------------|---------|------------:|
| Day        |    |  |
| 2020-12-02 | เมฆมาก  |          28 |
| 2020-12-03 | ฝนตก    |          27 |
| 2020-12-04 | แดดร้อน |          19 |
| 2020-12-05 | เมฆมาก  |          20 |
| 2020-12-06 | ฝนตก    |          25 |
| 2020-12-07 | ฝนตก    |          36 |
</div>
</details>


## 2.12 Finding data with Match & Contains
<pre>
- matching(string)      => <span style="color:red;">find the world start from the first string</span>
- contains(string)      => <span style="color:red;">find the world wildcard</span>
</pre>
``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

display(df['Event'].str.match('ฝนตก'))                      # match => true, not match => false
print("=============================================")
display(df[df['Event'].str.match('ฝนตก')])                  # filter match = true only
# display(df[df['Event'].str.match('ฝน')])                  # filter match = true only (start with 'ฝน')
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Day
# 2020-12-01    False
# 2020-12-02    False
# 2020-12-03     True
# 2020-12-04    False
# 2020-12-05    False
# 2020-12-06     True
# 2020-12-07     True
# 2020-12-08     True
# 2020-12-09    False
# 2020-12-10    False
# 2020-12-11     True
# 2020-12-12    False
# 2020-12-13    False
# 2020-12-14    False
# 2020-12-15    False
# 2020-12-16    False
# 2020-12-17     True
# 2020-12-18     True
# 2020-12-19    False
# 2020-12-20    False
# 2020-12-21    False
# 2020-12-22    False
# 2020-12-23     True
# 2020-12-24     True
# ...
# 2020-12-27    False
# 2020-12-28    False
# 2020-12-29     True
# 2020-12-30     True
# Name: Event, dtype: bool
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```

=============================================

|         | Temperature | WindSpeed | Event |
|------------|------------:|----------:|-------|
| Day        |  |  |  |
| 2020-12-03 |          27 |         4 | ฝนตก |
| 2020-12-06 |          25 |         6 | ฝนตก |
| 2020-12-07 |          36 |         4 | ฝนตก |
| 2020-12-08 |          28 |         6 | ฝนตก |
| 2020-12-11 |          26 |         4 | ฝนตก |
| 2020-12-17 |          20 |         8 | ฝนตก |
| 2020-12-18 |          18 |         5 | ฝนตก |
| 2020-12-23 |          34 |         3 | ฝนตก |
| 2020-12-24 |          29 |         4 | ฝนตก |
| 2020-12-26 |          25 |         8 | ฝนตก |
| 2020-12-29 |          31 |         1 | ฝนตก |
| 2020-12-30 |          35 |         2 | ฝนตก |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

display(df['Event'].str.match('ตก'))                      # match => true, not match => false
print("=============================================")
display(df[df['Event'].str.contains('ตก')])                  # filter match = true only
# display(df[df['Event'].str.match('ฝน')])                  # filter match = true only (start with 'ฝน')
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Day
# 2020-12-01    False
# 2020-12-02    False
# 2020-12-03    False
# 2020-12-04    False
# 2020-12-05    False
# 2020-12-06    False
# 2020-12-07    False
# 2020-12-08    False
# 2020-12-09    False
# 2020-12-10    False
# 2020-12-11    False
# 2020-12-12    False
# 2020-12-13    False
# 2020-12-14    False
# 2020-12-15    False
# 2020-12-16    False
# 2020-12-17    False
# 2020-12-18    False
# 2020-12-19    False
# 2020-12-20    False
# 2020-12-21    False
# 2020-12-22    False
# 2020-12-23    False
# 2020-12-24    False
# ...
# 2020-12-27    False
# 2020-12-28    False
# 2020-12-29    False
# 2020-12-30    False
# Name: Event, dtype: bool
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```

=============================================

|         | Temperature | WindSpeed | Event |
|------------|------------:|----------:|-------|
| Day        |  |  |  |
| 2020-12-03 |          27 |         4 | ฝนตก |
| 2020-12-06 |          25 |         6 | ฝนตก |
| 2020-12-07 |          36 |         4 | ฝนตก |
| 2020-12-08 |          28 |         6 | ฝนตก |
| 2020-12-11 |          26 |         4 | ฝนตก |
| 2020-12-17 |          20 |         8 | ฝนตก |
| 2020-12-18 |          18 |         5 | ฝนตก |
| 2020-12-23 |          34 |         3 | ฝนตก |
| 2020-12-24 |          29 |         4 | ฝนตก |
| 2020-12-26 |          25 |         8 | ฝนตก |
| 2020-12-29 |          31 |         1 | ฝนตก |
| 2020-12-30 |          35 |         2 | ฝนตก |
</div>
</details>


## 2.13 For Loop
- iterrows(): => output idx, row [value]

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

for idx, row in df.iterrows():
    print(f"อุณหภูมิ = {row.Temperature} ส่งผลให้เกิด {row.Event} ในวันที่ {idx.date()}")
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# อุณหภูมิ = 30 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-01
# อุณหภูมิ = 28 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-02
# อุณหภูมิ = 27 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-03
# อุณหภูมิ = 19 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-04
# อุณหภูมิ = 20 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-05
# อุณหภูมิ = 25 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-06
# อุณหภูมิ = 36 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-07
# อุณหภูมิ = 28 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-08
# อุณหภูมิ = 17 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-09
# อุณหภูมิ = 24 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-10
# อุณหภูมิ = 26 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-11
# อุณหภูมิ = 27 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-12
# อุณหภูมิ = 30 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-13
# อุณหภูมิ = 31 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-14
# อุณหภูมิ = 28 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-15
# อุณหภูมิ = 27 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-16
# อุณหภูมิ = 20 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-17
# อุณหภูมิ = 18 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-18
# อุณหภูมิ = 25 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-19
# อุณหภูมิ = 28 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-20
# อุณหภูมิ = 25 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-21
# อุณหภูมิ = 38 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-22
# อุณหภูมิ = 34 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-23
# อุณหภูมิ = 29 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-24
# อุณหภูมิ = 34 ส่งผลให้เกิด แดดร้อน ในวันที่ 2020-12-25
# ...
# อุณหภูมิ = 28 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-27
# อุณหภูมิ = 30 ส่งผลให้เกิด เมฆมาก ในวันที่ 2020-12-28
# อุณหภูมิ = 31 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-29
# อุณหภูมิ = 35 ส่งผลให้เกิด ฝนตก ในวันที่ 2020-12-30
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...
```
</div>
</details>


## 2.14 Condition

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

# วันใดบ้างที่มีอุณหภูมิ <= 20
display(df[df['Temperature'] <= 20])
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Temperature | WindSpeed | Event   |
|------------|------------:|----------:|---------|
| Day        |  |  |    |
| 2020-12-04 |          19 |         3 | แดดร้อน |
| 2020-12-05 |          20 |         5 | เมฆมาก  |
| 2020-12-09 |          17 |         5 | เมฆมาก  |
| 2020-12-17 |          20 |         8 | ฝนตก    |
| 2020-12-18 |          18 |         5 | ฝนตก    |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

# วันใดบ้างที่มีแดดร้อน
df[df['Event'] == 'แดดร้อน']
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Temperature | WindSpeed | Event   |
|------------|------------:|----------:|---------|
| Day        |  |  |    |
| 2020-12-01 |          30 |         9 | แดดร้อน |
| 2020-12-04 |          19 |         3 | แดดร้อน |
| 2020-12-10 |          24 |         6 | แดดร้อน |
| 2020-12-12 |          27 |         9 | แดดร้อน |
| 2020-12-13 |          30 |         2 | แดดร้อน |
| 2020-12-15 |          28 |         4 | แดดร้อน |
| 2020-12-16 |          27 |         7 | แดดร้อน |
| 2020-12-19 |          25 |         7 | แดดร้อน |
| 2020-12-25 |          34 |         5 | แดดร้อน  |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

# วันใดบ้างที่มีฝนตก และ มีอุณหภูมิ >= 35
display(df[(df['Event'] == 'ฝนตก') & (df['Temperature'] >= 35)])
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Temperature | WindSpeed | Event |
|------------|------------:|----------:|-------|
| Day        |  |  |  |
| 2020-12-07 |          36 |         4 | ฝนตก |
| 2020-12-30 |          35 |         2 | ฝนตก |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

# วันใดบ้างที่มีเมฆมาก หรือ อุณหภูมิ <=18
df[(df['Event'].str.contains('เมฆมาก')) | (df['Temperature'] <= 18)]
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Temperature | WindSpeed | Event   |
|------------|------------:|----------:|---------|
| Day        |  |  |    |
| 2020-12-02 |          28 |         8 | เมฆมาก  |
| 2020-12-05 |          20 |         5 | เมฆมาก  |
| 2020-12-09 |          17 |         5 | เมฆมาก  |
| 2020-12-14 |          31 |         5 | เมฆมาก  |
| 2020-12-18 |          18 |         5 | ฝนตก    |
| 2020-12-20 |          28 |         4 | เมฆมาก  |
| 2020-12-21 |          25 |         5 | เมฆมาก  |
| 2020-12-22 |          38 |         2 | เมฆมาก  |
| 2020-12-27 |          28 |         9 | เมฆมาก  |
| 2020-12-28 |          30 |         2 | เมฆมาก  |
</div>
</details>

``` python
# isin
import pandas as pd

df = pd.read_excel(r'ExportFile\dataupdate.xlsx', 'weather', index_col='Day')

# วันใดบ้างที่มีเมฆมาก หรือ อุณหภูมิ = 18 20 25
display(df[(df['Temperature'].isin([18, 20, 25]))])
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Temperature | WindSpeed | Event   |
|------------|------------:|----------:|---------|
| Day        |  |  |    |
| 2020-12-05 |          20 |         5 | เมฆมาก  |
| 2020-12-06 |          25 |         6 | ฝนตก    |
| 2020-12-17 |          20 |         8 | ฝนตก    |
| 2020-12-18 |          18 |         5 | ฝนตก    |
| 2020-12-19 |          25 |         7 | แดดร้อน |
| 2020-12-21 |          25 |         5 | เมฆมาก  |
| 2020-12-26 |          25 |         8 | ฝนตก    |
</div>
</details>


## 2.15 Sorting Data
### 2.15.1 with index

- sort_index()
- sort_index(ascending=False)

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')

display(df)
print("=============================================")
display(df.sort_index())                            # index is a String => A-Z ก-ฮ
print("=============================================")
df.sort_index(ascending=False, inplace=True)   # sort from most to least
display(df)    
```

<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| จาน                | เครื่องครัว             |   250 |      4 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| รถบังคับ           | ของเล่น                |   500 |      6 |

=============================================

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| External HardDisk | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| จาน                | เครื่องครัว             |   250 |      4 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| รถบังคับ           | ของเล่น                |   500 |      6 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |

=============================================

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| รถบังคับ           | ของเล่น                |   500 |      6 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| จาน                | เครื่องครัว             |   250 |      4 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |

</div>
</details>


### 2.15.2 with value

- sort_values('value_name')
- sort_values('value_name',ascending=False)

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')

display(df)
print("=============================================")
display(df.sort_values('Price'))                            # index is a String => A-Z ก-ฮ
print("=============================================")
df.sort_values('Price', ascending=False, inplace=True)   # sort from most to least
display(df)    
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| จาน                | เครื่องครัว             |   250 |      4 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| รถบังคับ           | ของเล่น                |   500 |      6 |

=============================================

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| จาน                | เครื่องครัว             |   250 |      4 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| รถบังคับ           | ของเล่น                |   500 |      6 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |

=============================================

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| รถบังคับ           | ของเล่น                |   500 |      6 |
| จาน                | เครื่องครัว             |   250 |      4 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
</div>
</details>


## 2.16 Adding Columns

- df['**columns_name**'] = '**values**'

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')

df['C_delivery'] = 100
df['C_total'] = df['Amount'] + df['C_delivery']
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|               | Category              | Price | Amount | C_delivery | C_total |
|-------------------|-----------------------|------:|-------:|-----------:|--------:|
| Name              |               |  |  |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |        100 |     110 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |        100 |     105 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |        100 |     107 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |        100 |     101 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |        100 |     100 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |        100 |     102 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |        100 |     108 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |        100 |     105 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |        100 |     105 |
| จาน                | เครื่องครัว             |   250 |      4 |        100 |     104 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |        100 |     107 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |        100 |     105 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |        100 |     107 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |        100 |     105 |
| รถบังคับ           | ของเล่น                |   500 |      6 |        100 |     106 |
</div>
</details>


## 2.17 Rename Columns

- df.**rename**(columns=**{'ColName_ORG':'ColName_New'}**, inplace=True)

- df.**rename**(columns=**{'ColName_ORG1':'ColName_New1', 'ColName_ORG2':'ColName_New2'}**, inplace=True)

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')

df['C_Delivery'] = 100
df['C_Total'] = df['Amount'] + df['C_Delivery']
display(df.head(3))
print("=============================================")
df.rename(columns={'Category':'Group', 'Price':'Cost'}, inplace=True)
display(df.head(3))
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|    | Category              | Price | Amount | C_Delivery | C_Total |
|--------|-----------------------|------:|-------:|-----------:|--------:|
| Name   |               |  |  |  |  |
| เมาส์  | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |        100 |     110 |
| ปากกา  | อุปกรณ์การเรียน        |   200 |      5 |        100 |     105 |
| โคมไฟ  | เครื่องใช้ในบ้าน        |  1200 |      7 |        100 |     107 |

=============================================

|   | Group                | Cost | Amount | C_Delivery | C_Total |
|-------|----------------------|-----:|-------:|-----------:|--------:|
| Name  |                 |  |  |  |  |
| เมาส์ | อุปกรณ์คอมพิวเตอร์     |  900 |     10 |        100 |     110 |
| ปากกา | อุปกรณ์การเรียน        |  200 |      5 |        100 |     105 |
| โคมไฟ | เครื่องใช้ในบ้าน        | 1200 |      7 |        100 |     107 |
</div>
</details>


## 2.18 Delete Columns

- df.drop(**'columns_name'**, **axis=1**, <inplace=True>)

> Remark : axis=0 (by index), axis=1 (by columns)

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')

display(df.drop('Amount', axis=1).head(3))
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|   | Category              | Price |
|-------|-----------------------|------:|
| Name  |               |  |
| เมาส์ | อุปกรณ์คอมพิวเตอร์     |   900 |
| ปากกา | อุปกรณ์การเรียน        |   200 |
| โคมไฟ | เครื่องใช้ในบ้าน        |  1200 |

</div>
</details>


## 2.19 Adding Rows

- df = df.append(df2)       => old_version (obsolete)
- df = pd.concat([df,df_new])

> Remark df and df2 are dataframe(s)

``` python
import pandas as pd
product = [
        ['หูฟัง (เพิ่ม)', 'อุปกรณ์คอม', 400, 20, 8000],
        ['สายชาร์จ (เพิ่ม)', 'อุปกรณ์คอม', 1400, 20, 28000]
          ]
cols = ['Name', 'Group', 'Cost', 'Qty', 'Summation']

df_new = pd.DataFrame(product, columns=cols)
df_new.set_index('Name', inplace=True)
display(df_new)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|              | Group        | Cost | Qty | Summation |
|------------------|-------------|-----:|----:|----------:|
| Name             |         |  |  |  |
| หูฟัง (เพิ่ม)     | อุปกรณ์คอม   |  400 |  20 |      8000 |
| สายชาร์จ (เพิ่ม) | อุปกรณ์คอม   | 1400 |  20 |     28000 |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')
df['Summation'] = df['Price'] * df['Amount']
df.rename(columns={'Category':'Group', 'Price':'Cost', 'Amount':'Qty'}, inplace=True)
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|               | Group                | Cost  | Qty | Summation |
|-------------------|--------------------|------:|----:|----------:|
| Name              |                 |   |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |  10 |      9000 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |   5 |      1000 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |   7 |      8400 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |   1 |       750 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |   0 |         0 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |   2 |      1000 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |   8 |      7992 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |   5 |      4750 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |   5 |     25000 |
| จาน                | เครื่องครัว             |   250 |   4 |      1000 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |   7 |    105000 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |   5 |       100 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |   7 |     17500 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |   5 |      4250 |
| รถบังคับ           | ของเล่น                |   500 |   6 |      3000 |

</div>
</details>

``` python
# Result

df = pd.concat([df,df_new])
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|                | Group                | Cost  | Qty | Summation |
|------------------- |--------------------|------:|----:|----------:|
| Name               |                 |   |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |  10 |      9000 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |   5 |      1000 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |   7 |      8400 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |   1 |       750 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |   0 |         0 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |   2 |      1000 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |   8 |      7992 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |   5 |      4750 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |   5 |     25000 |
| จาน                | เครื่องครัว             |   250 |   4 |      1000 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |   7 |    105000 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |   5 |       100 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |   7 |     17500 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |   5 |      4250 |
| รถบังคับ           | ของเล่น                |   500 |   6 |      3000 |
| หูฟัง (เพิ่ม)       | อุปกรณ์คอม             |   400 |  20 |      8000 |
| สายชาร์จ (เพิ่ม)    | อุปกรณ์คอม             |  1400 |  20 |     28000 |
</div>
</details>


## 2.20 Delete Rows

- df.drop(**rows_number**, **axis=0**, <inplace=True>)
- df.drop(**row_Name**, **axis=0**, <inplace=True>)

Remark : axis=0 (by index), axis=1 (by columns)

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx')
display(df)
print("=============================================")
display(df.drop([9,10], axis=0))        # Delete จาน ทีวี
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| จาน                | เครื่องครัว             |   250 |      4 |
| ทีวี               | เครื่องใช้ไฟฟ้า         | 15000 |      7 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| รถบังคับ           | ของเล่น                |   500 |      6 |

=============================================

|               | Category              | Price | Amount |
|-------------------|-----------------------|------:|-------:|
| Name              |               |  |  |
| เมาส์              | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| ปากกา              | อุปกรณ์การเรียน        |   200 |      5 |
| โคมไฟ              | เครื่องใช้ในบ้าน        |  1200 |      7 |
| ไมโครโฟน           | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| เครื่องซักผ้า       | เครื่องใช้ไฟฟ้า         |  3500 |      0 |
| เสื้อยืดคอกลม       | เสื้อผ้า               |   500 |      2 |
| กางเกงยีนต์         | เสื้อผ้า               |   999 |      8 |
| ตุ๊กตาหมีพูห์       | ของเล่น                |   950 |      5 |
| โซฟา               | เฟอร์นิเจอร์            |  5000 |      5 |
| ยางลบ              | อุปกรณ์การเรียน        |    20 |      5 |
| External HardDisk  | อุปกรณ์คอมพิวเตอร์     |  2500 |      7 |
| คีย์บอร์ด          | อุปกรณ์คอมพิวเตอร์     |   850 |      5 |
| รถบังคับ           | ของเล่น                |   500 |      6 |
</div>
</details>


## 2.21 Finding summation data (columns, rows)

<pre>
- df.sum()          axis=0
- df.sum(axis=1)    axis=1

- axis = 0 คอลัมน์ (ผลรวมบนลงล่าง **ทีละแถว**) => บวกข้อมูล*ทีละแถว* ของคอลัมน์นั้นๆ
- axis = 1 แถว (ผลรวมซ้ายไปขวา **ทีละคอลัมน์**) => บวกข้อมูล*ทีละคอลัมน์"* ของแถวนั้นๆ
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Stock.xlsx', index_col='Name')
display(df.head())
print("=============================================")
display(df.sum(axis=0))
print("=============================================")
display(df.sum(axis=1, numeric_only=True))
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|            | Category              | Price | Amount |
|----------------|----------------------|------:|-------:|
| Name           |               |  |  |
| เมาส์          | อุปกรณ์คอมพิวเตอร์     |   900 |     10 |
| ปากกา          | อุปกรณ์การเรียน        |   200 |      5 |
| โคมไฟ          | เครื่องใช้ในบ้าน        |  1200 |      7 |
| ไมโครโฟน       | เครื่องใช้ไฟฟ้า         |   750 |      1 |
| เครื่องซักผ้า   | เครื่องใช้ไฟฟ้า         |  3500 |      0 |

=============================================

Category    อุปกรณ์คอมพิวเตอร์อุปกรณ์การเรียนเครื่องใช้ในบ...
Price                                                   33119
Amount                                                     77
dtype: object

=============================================

``` python
# Name
# เมาส์                  910
# ปากกา                  205
# โคมไฟ                 1207
# ไมโครโฟน               751
# เครื่องซักผ้า         3500
# เสื้อยืดคอกลม          502
# กางเกงยีนต์           1007
# ตุ๊กตาหมีพูห์          955
# โซฟา                  5005
# จาน                    254
# ทีวี                 15007
# ยางลบ                   25
# External HardDisk     2507
# คีย์บอร์ด              855
# รถบังคับ               506
# dtype: int64
```
</div>
</details>


## 2.22 Missing value

<pre>
- df.isnull()
    - ค่า True แสดงว่ามีข้อมูลไม่ครบหรือสูญหาย
    - ค่า False แสดงว่าข่อมูลครบ

- df.isnull().any() - หาว่าคอลัมน์ใดที่มีค่าว่าง
- df.isnull().sum() - มีค่าว่างกี่แถว
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
display(df.isnull())        # เชคว่าเป็นค่าว่างหรือไม่ True = เป็น , False = ไม่ว่าง
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|        | Job        | Age  | Salary    | Bonus | Address |
|------------|-----------|-----:|----------:|------:|--------|
| Name       |         |   |     |  |  |
| อาทิตย์     | Programmer | 20.0 |  30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |        |
| จักรพงษ์    | Developer  |  NaN |  32000.0 |   0.1 |        |
| สุรชัย      |            | 23.0 |  40000.0 |   0.1 |        |
| ทศพล       | Sale       | 29.0 |  40000.0 |   0.1 |        |
| จินตนา     | Manager    |  NaN | 450000.0 |   0.1 |        |
| เกษมสันต์   | Maketing   | 34.0 |  60000.0 |   0.1 |        |
| ชลธิชา     |            | 26.0 | 100000.0 |   0.1 |        |
| เกษมสันต์   | Maketing   | 34.0 |  60000.0 |   0.1 |        |
| ทศพล       | Sale       | 29.0 |  40000.0 |   0.1 |        |

=============================================

|        | Job   | Age   | Salary | Bonus | Address |
|------------|-------|------|--------|-------|--------|
| Name       |    |    |  |  |  |
| อาทิตย์     | False | False | False  | False | True   |
| เกียรติศักดิ์ | False | False | True   | False | True   |
| จักรพงษ์    | False | True  | False  | False | True   |
| สุรชัย      | True  | False | False  | False | True   |
| ทศพล       | False | False | False  | False | True   |
| จินตนา     | False | True  | False  | False | True   |
| NaN        | True  | True  | True   | True  | True   |
| เกษมสันต์   | False | False | False  | False | True   |
| ชลธิชา     | True  | False | False  | False | True   |
| เกษมสันต์   | False | False | False  | False | True   |
| ทศพล       | False | False | False  | False | True   |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')

display(df.isnull().any())      # เชคว่า ทั้งคอลัมน์ เป็นค่าว่างหรือไม่ True = เป็น , False = ไม่ว่าง
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Job        True
# Age        True
# Salary     True
# Bonus      True
# Address    True
# dtype: bool
```

``` python
# Job         True
# Age         True
# Salary      True
# Bonus       True
# Address    False
# dtype: bool
```
</div>
</details>

``` python
# เชคว่ามีค่าว่างกี่แถว
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')

display(df.isnull().sum())      # เชคแต่ละคอลัมน์ว่า มีค่าว่างกี่แถว
display(df.notnull().sum())     # เชคแต่ละคอลัมน์ว่า มีค่าที่ระบุกี่แถว
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

``` python
# Job         3
# Age         3
# Salary      2
# Bonus       1
# Address    11
# dtype: int64
```
``` python
# Job         8
# Age         8
# Salary      9
# Bonus      10
# Address     0
# dtype: int64
```
</div>
</details>


## 2.23 Manage missing value

- แทนที่ด้วยค่าเฉลี่ยข้อมูลทั้งหมด
- แทนที่ด้วยค่าตรงๆที่กำหนดขึ้นมา
- แทนที่ด้วยค่าก่อนหน้า
- แทนที่ด้วยค่าถัดไป
- ลบข้อมูล

### 2.23.1 Replace with AVG

<pre>
- df[ColName] = df[ColName].fillna(df[ColName].mean())
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')

display(df.describe())
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|        | Age   | Salary        | Bonus | Address |
|--------|------:|--------------:|------:|--------|
| count  |  8.0  |  9.0          | 10.0  | 0.0     |
| mean   | 26.625| 94666.666667  | 0.1   | NaN     |
| std    |  5.998| 134985.184372 | 0.0   | NaN     |
| min    | 18.0  | 30000.0       | 0.1   | NaN     |
| 25%    | 22.25 | 40000.0       | 0.1   | NaN     |
| 50%    | 27.5  | 40000.0       | 0.1   | NaN     |
| 75%    | 30.25 | 60000.0       | 0.1   | NaN     |
| max    | 34.0  | 450000.0      | 0.1   | NaN     |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")

df['Salary'] = df['Salary'].fillna(df['Salary'].mean()) 
# คอลัมน์ Salary เติมข้อมูล (fillna) ด้วย ค่าเฉลี่ย >> แล้วทับที่ คอลัมน์ Salary
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |  NaN       |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |        |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |        |
| สุรชัย       |    NaN        | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |        |
| NaN         |   NaN         |  NaN |       NaN |   NaN |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      |   NaN         | 26.0 |  100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |

=============================================

|         | Job        | Age  | Salary        | Bonus | Address |
|------------ |----------- |-----:|--------------:|------:|--------|
| Name        |   NaN      |   |         |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.000000 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |   94666.666667 |   0.1 |        |
| จักรพงษ์     | Developer  |  NaN |   32000.000000 |   0.1 |        |
| สุรชัย       |  NaN          | 23.0 |   40000.000000 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.000000 |   0.1 |        |
| จินตนา      | Manager    |  NaN |  450000.000000 |   0.1 |        |
| NaN         |    NaN        |  NaN |   94666.666667 |   NaN |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.000000 |   0.1 |        |
| ชลธิชา      |   NaN         | 26.0 |  100000.000000 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.000000 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.000000 |   0.1 |        |
</div>
</details>


### 2.23.2 Replace with determine data

<pre>
- df[ColName] = df[ColName].fillna(value)
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
# เติมค่าว่าง คอลัมน์เงินเดือนด้วย 18000
df['Salary'] = df['Salary'].fillna(18000)
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |        |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |        |
| สุรชัย       |  NaN          | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |        |
| NaN         |  NaN          |  NaN |       NaN |   NaN |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      |            | 26.0 |  100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |

=============================================

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |   18000.0 |   0.1 |        |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |        |
| สุรชัย       |            | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |        |
| NaN         |            |  NaN |   18000.0 |   NaN |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      |            | 26.0 |  100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
</div>
</details>


### 2.23.3 Replace with previous data

<pre>
- df[ColName] = df[ColName].fillna(method='pad', inplace=True)
- df = df.fillna(method='pad', inplace=True)                            # มีผลทุกคอลัมน์
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
# แทนค่าว่าง (ทุกคอลัมน์) ด้วยค่าก่อนหน้า
df = df.fillna(method='pad')
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |  NaN      |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |   NaN    |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |   NaN     |
| สุรชัย       |    NaN        | 23.0 |   40000.0 |   0.1 |  NaN      |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |  NaN      |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |   NaN     |
| NaN         |   NaN         |  NaN |       NaN |   NaN | NaN       |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |  NaN      |
| ชลธิชา      |     NaN       | 26.0 |  100000.0 |   0.1 |  NaN      |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |  NaN      |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |  NaN      |

=============================================
D:\Users\sutripat.ng\AppData\Local\Temp\ipykernel_22920\2164306661.py:7: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df = df.fillna(method='pad')

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |   30000.0 |   0.1 |        |
| จักรพงษ์     | Developer  | 18.0 |   32000.0 |   0.1 |        |
| สุรชัย       | Developer  | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    | 29.0 |  450000.0 |   0.1 |        |
| NaN         | Manager    | 29.0 |  450000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      | Maketing   | 26.0 | 100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |

</div>
</details>


### 2.23.4 Replace with next data

<pre>
- df[ColName].fillna(method='bfill', inplace=True)
- df.fillna(method='pad', inplace=True)               # มีผลทุกคอลัมน์
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
# แทนค่าว่าง (ทุกคอลัมน์) ด้วยค่าถัดไป
df = df.fillna(method='bfill')
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |        |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |        |
| สุรชัย       |  NaN          | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |        |
| NaN         |   NaN         |  NaN |       NaN |   NaN |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      |    NaN        | 26.0 |  100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
=============================================
D:\Users\sutripat.ng\AppData\Local\Temp\ipykernel_22920\1766016403.py:7: FutureWarning: DataFrame.fillna with 'method' is deprecated and will raise in a future version. Use obj.ffill() or obj.bfill() instead.
  df = df.fillna(method='bfill')

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |   32000.0 |   0.1 |        |
| จักรพงษ์     | Developer  | 23.0 |   32000.0 |   0.1 |        |
| สุรชัย       | Sale       | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    | 34.0 |  450000.0 |   0.1 |        |
| NaN         | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      | Maketing   | 26.0 |  100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
</div>
</details>


### 2.23.5 Delete all

<pre>
df.dropna(inplace=True)
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
# ถ้าแถวใด มีค่าว่าง จะทำการลบทิ้งแถวนั้น => ทุกแถวมีค่าว่าง
df = df.dropna()
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |        |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |        |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |        |
| สุรชัย       |            | 23.0 |   40000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |        |
| NaN         |            |  NaN |       NaN |   NaN |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ชลธิชา      |            | 26.0 |  100000.0 |   0.1 |        |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |        |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |        |

=============================================

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
</div>
</details>


### 2.23.6 Delete some row(s)

<pre>
df.dropna(subset=['ColName1','ColName2'], inplace=True)
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
# ถ้าคอลัมน์ Age หรือ Job มีแถวใด เป็นค่าว่าง => ให้ลบแถวนั้น (แสดง Age และ Job ที่มีค่า)
# [SQL : where Age is not null and Job is not null]
df = df.dropna(subset=['Age','Job'])
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary     | Bonus | Address |
|------------ |----------- |-----:|-----------:|------:|--------|
| Name        |         |   |      |  |  |
| อาทิตย์      | Programmer | 20.0 |   30000.0 |   0.1 |  NaN      |
| เกียรติศักดิ์ | Programmer | 18.0 |       NaN |   0.1 |   NaN     |
| จักรพงษ์     | Developer  |  NaN |   32000.0 |   0.1 |   NaN     |
| สุรชัย       |    NaN        | 23.0 |   40000.0 |   0.1 |  NaN      |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |  NaN      |
| จินตนา      | Manager    |  NaN |  450000.0 |   0.1 |   NaN     |
| NaN         |    NaN        |  NaN |       NaN |   NaN |  NaN      |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |    NaN    |
| ชลธิชา      |   NaN         | 26.0 |  100000.0 |   0.1 | NaN       |
| เกษมสันต์    | Maketing   | 34.0 |   60000.0 |   0.1 |   NaN     |
| ทศพล        | Sale       | 29.0 |   40000.0 |   0.1 |  NaN      |

=============================================

|         | Job       | Age  | Salary   | Bonus | Address |
|------------ |---------- |-----:|---------:|------:|--------|
| Name        |        |   |    |  |  |
| อาทิตย์      | Programmer | 20.0 | 30000.0 | 0.1   |  NaN      |
| เกียรติศักดิ์ | Programmer | 18.0 |      NaN | 0.1   |   NaN     |
| ทศพล        | Sale       | 29.0 | 40000.0 | 0.1   |  NaN      |
| เกษมสันต์    | Maketing   | 34.0 | 60000.0 | 0.1   |  NaN      |
| เกษมสันต์    | Maketing   | 34.0 | 60000.0 | 0.1   |  NaN      |
| ทศพล        | Sale       | 29.0 | 40000.0 | 0.1   |   NaN     |
</div>
</details>


### 23.7 Delete some column(s)

<pre>
df.dropna(axis='columns',inplaceTrue)
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
# ถ้าคอลัมน์ใด มีค่าว่าง => ให้ลบคอลัมน์นั้น => ลบหมดเลย เหลือแต่ index
df = df.dropna(axis='columns')
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|         | Job        | Age  | Salary    | Bonus | Address |
|------------ |----------- |----: |---------: |------:|--------|
| Name        |         |   |     |  |  |
| อาทิตย์      | Programmer | 20.0 | 30000.0  | 0.1   | NaN      |
| เกียรติศักดิ์ | Programmer | 18.0 | NaN        | 0.1   | NaN      |
| จักรพงษ์      | Developer  | NaN    | 32000.0  | 0.1   | NaN      |
| สุรชัย        | NaN          | 23.0 | 40000.0  | 0.1   | NaN      |
| ทศพล          | Sale       | 29.0 | 40000.0  | 0.1   | NaN      |
| จินตนา        | Manager    | NaN    | 450000.0 | 0.1   | NaN      |
| NaN             | NaN          | NaN    | NaN        | NaN     | NaN      |
| เกษมสันต์     | Maketing   | 34.0 | 60000.0  | 0.1   | NaN      |
| ชลธิชา        | NaN          | 26.0 | 100000.0 | 0.1   | NaN      |
| เกษมสันต์     | Maketing   | 34.0 | 60000.0  | 0.1   | NaN      |
| ทศพล          | Sale       | 29.0 | 40000.0  | 0.1   | NaN      |

=============================================

| Name        |
|------------ |
| อาทิตย์      |
| เกียรติศักดิ์ |
| จักรพงษ์      |
| สุรชัย        |
| ทศพล          |
| จินตนา        |
| NaN           |
| เกษมสันต์     |
| ชลธิชา        |
| เกษมสันต์     |
| ทศพล          |
</div>
</details>


## 24. Remove duplicate

<pre>
- df[df.duplicated()]   => เช็คค่าซ้ำ
- df.drop_duplicates(inplace=True)
</pre>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx', index_col='Name')
display(df)
print("=============================================")
display(df[df.duplicated()] )    # เช็คว่า ซ้ำมีใครบ้าง
print("=============================================")
df = df.drop_duplicates()
display(df)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|        | Job        | Age  | Salary    | Bonus | Address |
|------------|------------|------|----------|-------|---------|
| Name       |         |   |     |  |  |
| อาทิตย์     | Programmer | 20.0 | 30000.0 | 0.1   | NaN     |
| เกียรติศักดิ์ | Programmer | 18.0 | NaN      | 0.1   | NaN     |
| จักรพงษ์     | Developer  | NaN  | 32000.0 | 0.1   | NaN     |
| สุรชัย       | NaN        | 23.0 | 40000.0 | 0.1   | NaN     |
| ทศพล        | Sale       | 29.0 | 40000.0 | 0.1   | NaN     |
| จินตนา       | Manager    | NaN  | 450000.0| 0.1   | NaN     |
| NaN         | NaN        | NaN  | NaN      | NaN   | NaN     |
| เกษมสันต์    | Maketing   | 34.0 | 60000.0 | 0.1   | NaN     |
| ชลธิชา       | NaN        | 26.0 | 100000.0| 0.1   | NaN     |
| เกษมสันต์    | Maketing   | 34.0 | 60000.0 | 0.1   | NaN     |
| ทศพล        | Sale       | 29.0 | 40000.0 | 0.1   | NaN     |

=============================================

|        | Job      | Age  | Salary   | Bonus | Address |
|------------|----------|------|---------|-------|---------|
| Name       |       |   |    |  |  |
| เกษมสันต์  | Maketing | 34.0 | 60000.0 | 0.1   | NaN     |
| ทศพล      | Sale     | 29.0 | 40000.0 | 0.1   | NaN     |

=============================================

|        | Job       | Age  | Salary    | Bonus | Address |
|------------|-----------|------|----------|-------|---------|
| Name       |        |   |     |  |  |
| อาทิตย์    | Programmer | 20.0 | 30000.0  | 0.1   | NaN     |
| เกียรติศักดิ์ | Programmer | 18.0 | NaN      | 0.1   | NaN     |
| จักรพงษ์    | Developer  | NaN  | 32000.0  | 0.1   | NaN     |
| สุรชัย      | NaN       | 23.0 | 40000.0  | 0.1   | NaN     |
| ทศพล       | Sale      | 29.0 | 40000.0  | 0.1   | NaN     |
| จินตนา     | Manager   | NaN  | 450000.0 | 0.1   | NaN     |
| NaN        | NaN       | NaN  | NaN      | NaN   | NaN     |
| เกษมสันต์  | Maketing  | 34.0 | 60000.0  | 0.1   | NaN     |
| ชลธิชา     | NaN       | 26.0 | 100000.0 | 0.1   | NaN     |
</div>
</details>


## 25. Groupby

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx')
display(df)
print("=============================================")
df_m = df.groupby('Job').agg({'Salary': ['min','max','mean'], 'Age':['size','count']}).reset_index()
display(df_m)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|   | Name        | Job        | Age  | Salary     | Bonus | Address |
|---|------------|------------|------|-----------|-------|---------|
| 0 | อาทิตย์     | Programmer | 20.0 | 30000.0  | 0.1   | NaN     |
| 1 | เกียรติศักดิ์ | Programmer | 18.0 | NaN      | 0.1   | NaN     |
| 2 | จักรพงษ์    | Developer  | NaN  | 32000.0  | 0.1   | NaN     |
| 3 | สุรชัย      | NaN        | 23.0 | 40000.0  | 0.1   | NaN     |
| 4 | ทศพล       | Sale       | 29.0 | 40000.0  | 0.1   | NaN     |
| 5 | จินตนา     | Manager    | NaN  | 450000.0 | 0.1   | NaN     |
| 6 | NaN        | NaN        | NaN  | NaN      | NaN   | NaN     |
| 7 | เกษมสันต์   | Maketing   | 34.0 | 60000.0  | 0.1   | NaN     |
| 8 | ชลธิชา     | NaN        | 26.0 | 100000.0 | 0.1   | NaN     |
| 9 | เกษมสันต์   | Maketing   | 34.0 | 60000.0  | 0.1   | NaN     |
| 10| ทศพล       | Sale       | 29.0 | 40000.0  | 0.1   | NaN     |


=============================================

|   | Job        | Salary |  |  | Age |  |
|---|------------|-----------|-----------|------------|---------|-----------|
|   | Job        | min | max | mean | size | count |
| 0 | Developer  | 32000.0   | 32000.0   | 32000.0    | 1       | 0         |
| 1 | Maketing   | 60000.0   | 60000.0   | 60000.0    | 2       | 2         |
| 2 | Manager    | 450000.0  | 450000.0  | 450000.0   | 1       | 0         |
| 3 | Programmer | 30000.0   | 30000.0   | 30000.0    | 2       | 2         |
| 4 | Sale       | 40000.0   | 40000.0   | 40000.0    | 2       | 2         |
</div>
</details>

``` python
import pandas as pd

df = pd.read_excel(r'ExportFile\Employee.xlsx')
df_m = df.groupby('Job').agg({'Salary': ['min','max','mean'], 'Age':['size','count']}).reset_index()
df_m.columns = ['_'.join(col).strip('_') for col in df_m.columns]

display(df_m)
```
<details>
<summary> Output </summary>

<div style="margin-left:1em; margin-top:1em">

|   | Job        | Salary_min | Salary_max | Salary_mean | Age_size | Age_count |
|---|------------|-----------|-----------|------------|---------|-----------|
| 0 | Developer  | 32000.0   | 32000.0   | 32000.0    | 1       | 0         |
| 1 | Maketing   | 60000.0   | 60000.0   | 60000.0    | 2       | 2         |
| 2 | Manager    | 450000.0  | 450000.0  | 450000.0   | 1       | 0         |
| 3 | Programmer | 30000.0   | 30000.0   | 30000.0    | 2       | 2         |
| 4 | Sale       | 40000.0   | 40000.0   | 40000.0    | 2       | 2         |
</div>
</details>




