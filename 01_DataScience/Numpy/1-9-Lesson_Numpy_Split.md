# 9. Split

- **Split 1 dim :** `np.split(a, split_value)`     where "a" is a array / *split have to divisible*.
- **Split >=2 dims :** `np.[v/h]split(a, split_value)`     where "a" is a array / *split have to divisible*.


``` python
# Split 1 dim
import numpy as np

a = np.arange(1,21)
b = np.split(a,4)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
# =============================================
# [array([1, 2, 3, 4, 5]), array([ 6,  7,  8,  9, 10]), array([11, 12, 13, 14, 15]), array([16, 17, 18, 19, 20])]
```
</details>


``` python
# Split >=2 dims
import numpy as np

a = np.arange(1,21).reshape(5,4)
b = np.hsplit(a, 4)
c = np.vsplit(a, 5)

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]]s
# =============================================
# [array([[ 1],
#        [ 5],
#        [ 9],
#        [13],
#        [17]]), array([[ 2],
#        [ 6],
#        [10],
#        [14],
#        [18]]), array([[ 3],
#        [ 7],
#        [11],
#        [15],
#        [19]]), array([[ 4],
#        [ 8],
#        [12],
#        [16],
#        [20]])]
# =============================================
# [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]]), array([[ 9, 10, 11, 12]]), array([[13, 14, 15, 16]]), array([[17, 18, 19, 20]])]
```
</details>

