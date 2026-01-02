# 3. Slice (Query data)

- **1 dimension :** a[2:], a[:4]
- **2 dimensions :** a[1:3, 1:]

``` python
# one dimension
import numpy as np

a = np.array([1,11,7,6,9])

print(a[2:])    # From index=2 to the last character  (start with index=0)
print("=============================================")
print(a[:4])    # From the first character to index=3 (4-1) -> a[:m] -> size=m (index=0 to m-1)
```
<details>
<summary> Output </summary>

``` python
# [7 6 9]
# =============================================
# [ 1 11  7  6]
```
</details>


``` python
# two dimensions
import numpy as np

a = np.array([[1,2,3,4], 
              [5,6,7,8], 
              [9,10,11,12]])

print(a[1:3, 1:])       # select row index = 1 to 2 (3-1), col index = 1 to last.
```
<details>
<summary> Output </summary>

``` python
[[ 6  7  8]
 [10 11 12]]
```
</details>

