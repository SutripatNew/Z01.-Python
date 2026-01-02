# 7. Dot product

- **Dot product :** a.dot(b) where a and b are arrays #multiple matrix

``` python
# Dot product
import numpy as np

a = np.array([[1,2], [3,4]])
b = np.array([[11,12], [13,14]])
c = a.dot(b)

print(a)
print("=============================================")
print(b)
print("=============================================")
print(c)
```
<details>
<summary> Output </summary>

``` python
# [[1 2]
#  [3 4]]
# =============================================
# [[11 12]
#  [13 14]]
# =============================================
# [[37 40]
#  [85 92]]
```
</details>

