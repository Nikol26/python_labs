# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

## Задание 1 — arrays.py
## min_max
<pre><code>
  def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise 'ValueError'
    mn = min(nums)
    mx = max(nums)
    return (mn, mx)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))
</code></pre>
<img width="676" height="475" alt="laba_2_1 1" src="https://github.com/user-attachments/assets/f3703597-4959-4a01-9831-a15a841ab9d1" />

## unique_sorted
<pre><code>
  def unique_sorted(nums):
    return sorted(set(nums))
print(unique_sorted([3,1,2,1,3]))
print(unique_sorted([]))
print(unique_sorted([-1,-1,0,2,2]))
print(unique_sorted([1.0,1,2.5,2.5,0]))
</code></pre>
<img width="503" height="294" alt="laba_2_1 2" src="https://github.com/user-attachments/assets/72b88ea5-d04f-4861-97de-fe6c058db92c" />

## flatten
<pre><code>
  def flatten(mat: list[list | tuple]) -> list:
    answ = []
    for container in mat:
        if not isinstance(container, (list, tuple)):
            raise TypeError("The element must be be a list or tuple")
        for item in container:
            answ.append(item)
    return answ
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
</code></pre>
<img width="655" height="445" alt="laba_2_1 3" src="https://github.com/user-attachments/assets/1acef4b4-a4b9-47aa-9547-17fd0cc96a76" />

  
  






