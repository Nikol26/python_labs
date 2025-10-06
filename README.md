# Лабораторная работа 2

## задание 1
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
<img width="668" height="241" alt="laba_2_1 1" src="https://github.com/user-attachments/assets/ec98472a-9755-4f68-ba64-ced51ec0a367" />



