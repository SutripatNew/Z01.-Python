# 6. Function for Statistic

- **Function about statistic** # 1 or 2 dimension(s)

``` python
# Function about statistic 1 dimension
# sum, prod, mean, max, min, position of max/min
import numpy as np

a = np.array([10,5,4,6,99,100,50,30])

print(f"a: {a}")
print("=============================================")
print(f"sum: {a.sum()}")
print("=============================================")
print(f"product: {a.prod()}")
print("=============================================")
print(f"mean: {a.mean()}")
print("=============================================")
print(f"max: {a.max()}")
print("=============================================")
print(f"min: {a.min()}")
print("=============================================")
print(f"position (index) of max: {a.argmax()}")
print("=============================================")
print(f"position (index) of min: {a.argmin()}")
```
<details>
<summary> Output </summary>

``` python
# a: [ 10   5   4   6  99 100  50  30]
# =============================================
# sum: 304
# =============================================
# product: 17820000000
# =============================================
# mean: 38.0
# =============================================
# max: 100
# =============================================
# min: 4
# =============================================
# position (index) of max: 5
# =============================================
# position (index) of min: 2
```
</details>


``` python
## Function about statistic 2 dimensions
# sum, prod, mean, max, min, position of max/min
# axis 0 (Vertical), axis 1 (Horizontal)
import numpy as np

a = np.array([[10,20,30], [40,50,90], [80,100,5]])

print(f"a: {a}")
print("=============================================")
print(f"sum (align vertical (แนวตั้ง)): {np.sum(a, axis=0)}")
print("=============================================")
print(f"product (align vertical (แนวตั้ง)): {np.prod(a, axis=0)}")
print("=============================================")
print(f"mean (align horizontal (แนวนอน)): {np.mean(a, axis=1)}")
print("=============================================")
print(f"max (align horizontal (แนวนอน)): {np.max(a, axis=1)}")
print("=============================================")
print(f"min (align horizontal (แนวนอน)): {np.min(a, axis=1)}")
print("=============================================")
print(f"position (index) of max (align horizontal (แนวนอน)): {np.argmax(a, axis=1)}")
print("=============================================")
print(f"position (index) of min (align horizontal (แนวนอน)): {np.argmin(a, axis=1)}")
```
<details>
<summary> Output </summary>

``` python
# a: [[ 10  20  30]
#  [ 40  50  90]
#  [ 80 100   5]]
# =============================================
# sum (align vertical (แนวตั้ง)): [130 170 125]
# =============================================
# product (align vertical (แนวตั้ง)): [ 32000 100000  13500]
# =============================================
# mean (align horizontal (แนวนอน)): [20.         60.         61.66666667]
# =============================================
# max (align horizontal (แนวนอน)): [ 30  90 100]
# =============================================
# min (align horizontal (แนวนอน)): [10 40  5]
# =============================================
# position (index) of max (align horizontal (แนวนอน)): [2 2 1]
# =============================================
# position (index) of min (align horizontal (แนวนอน)): [0 0 2]
```
</details>

