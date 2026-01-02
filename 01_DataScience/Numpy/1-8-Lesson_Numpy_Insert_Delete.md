# 8. Insert / Delete

- **Insert 1 dim:** `np.insert(a, index, value)`     where "a" is a array
- **Insert >=2 dims:** `np.insert(a, index, value, axis=...)`     where "a" is a array
- **Delete :** `np.delete(a, index)`            where "a" is a array
- **Delete >=2 dims:** `np.delete(a, index, axis=...)`            where "a" is a array

``` python
# insert 1 dim : can indicate position of elements
import numpy as np

a = np.array([1,2,4,5,8])
b = np.append(a, 100)
c = np.insert(a, 1, 100)    # insert index = 1 with value = 100
d = np.insert(a, (1,3), (100,200))
print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
print("=============================================")
print(d)
```
<details>
<summary> Output </summary>

``` python
[1 2 4 5 8]
=============================================
[  1   2   4   5   8 100]
=============================================
[  1 100   2   4   5   8]
=============================================
[  1 100   2   4 200   5   8]
```
</details>


``` python
# insert 2 dims : can indicate position of elements
import numpy as np

a = np.array([[1,2], [10,11]])
b = np.insert(a, 1, 100, axis=0)
c = np.insert(a, 1, [800,900], axis=1)
print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [[ 1  2]
#  [10 11]]
# =============================================
# [[  1   2]
#  [100 100]
#  [ 10  11]]
# =============================================
# [[  1 800   2]
#  [ 10 900  11]]
```
</details>


``` python
# delete 1 dim
import numpy as np

a = np.arange(1,11)
b = np.delete(a, 2)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [ 1  2  3  4  5  6  7  8  9 10]
# =============================================
# [ 1  2  4  5  6  7  8  9 10]
```
</details>


``` python
# delete 2 dim
import numpy as np

a = np.arange(1,13).reshape(4,3)
b = np.delete(a, 2, axis=0)

print(a)
print("=============================================")
print(b)
```
<details>
<summary> Output </summary>

``` python
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
# =============================================
# [[ 1  2  3]
#  [ 4  5  6]
#  [10 11 12]]
```
</details>

