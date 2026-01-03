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

