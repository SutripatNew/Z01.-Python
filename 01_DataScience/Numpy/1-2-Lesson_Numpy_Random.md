# 2. Random

- **rand :** `numpy.random.rand(d0, d1, ..., dn)`   # d0,...dn are dimension of matrix
- **randn :** `np.random.randn(d0, d1, ..., dn)`    # Standard normal distribution (mean 0, std 1)
- **randint :** `np.random.randint(low, high=None, size=None, dtype=int)` # [low,hitght)
- **shuffle :** `np.random.shuffle(x)`              # shuffle order in arr (list)


``` python
# rand  -> Random value [0, 1)
import numpy as np

a = np.random.rand()        # not indicate = value (0 dim)
b = np.random.rand(2)        # 1 dim
c = np.random.rand(2,3)     # 2 dim

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# 0.6697208511638658
# =============================================
# [0.57925947 0.08354378]
# =============================================
# [[0.59889974 0.2977149  0.61128553]
#  [0.34440612 0.69365838 0.87989882]]
```
</details>


``` python
# randn
import numpy as np

a = np.random.randn()        # not indicate = value (0 dim)
b = np.random.randn(2)        # 1 dim
c = np.random.randn(2,3)     # 2 dim

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# 1.2612488680530454
# =============================================
# [1.53260329 0.37524792]
# =============================================
# [[-0.10007651 -0.31421211 -1.09793232]
#  [ 0.17918088  0.26968506 -0.05270229]]
```
</details>


``` python
# randint
import numpy as np

a = np.random.randint(1, 11, 5)         # low, hight, size -> [low, hight)
b = np.random.randint(2)
c = np.random.randint(2,3)

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [10  9  3  2  4]
# =============================================
# 1
# =============================================
# 2
```
</details>


``` python
# choice
import numpy as np

a = np.random.choice([1,2,3,4], 2)  # random values in list, size
print(a)
```
<details>
<summary> Output </summary>

``` python
# [3 1]
```
</details>


``` python
# shuffle
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)
```
<details>
<summary> Output </summary>

``` python
# [2 3 5 1 4]
```
</details>

