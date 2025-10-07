# ЛР2 — Коллекции и матрицы (list/tuple/set/dict)

# Задание A — arrays.py
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
<img width="623" height="438" alt="lab_2_1 1" src="https://github.com/user-attachments/assets/50859b00-edd9-44db-8f02-497131c2052a" />


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
<img width="705" height="404" alt="lab_2_1 3" src="https://github.com/user-attachments/assets/c925e418-6be6-4187-9a19-824a259e38af" />

# Задание B — matrix.py
## transpose
<pre><code>
  def check_rectangular(mat):
    if not mat:
        return True
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            return False
    return True
def transpose(mat):
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    if not mat:
        return []
    return [list(row) for row in zip(*mat)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
</code></pre>
<img width="553" height="503" alt="lab_2_2_1" src="https://github.com/user-attachments/assets/d1deee4a-62bd-4c2d-8d2c-d972ade9887d" />

## row_sums
<pre><code>
  def check_rectangular(mat):
    if not mat:
        return True
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            return False
    return True
def row_sums(mat):
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    return [sum(row) for row in mat]
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
</code></pre>
<img width="629" height="485" alt="laba_2_2_2" src="https://github.com/user-attachments/assets/52e0e983-afb9-4b6a-9f78-452e2e192aaf" />

## col_sums
<pre><code>
  def check_rectangular(mat):
    if not mat:
        return True
    length = len(mat[0])
    for row in mat:
        if len(row) != length:
            return False
    return True
def col_sums(mat):
    if not check_rectangular(mat):
        raise ValueError("Рваная матрица")
    if not mat:
        return []
    return [sum(col) for col in zip(*mat)]
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
</code></pre>
<img width="656" height="490" alt="laba_2_2_3" src="https://github.com/user-attachments/assets/38d6d028-c6b9-406c-8547-41aeba783414" />

# Задание C — tuples.py
<pre><code>
def format_record(student: tuple[str, str, float]) -> str:
    if len(student) != 3: #проверяем, что ровно 3 элемента в кортеже
        return "ValueError"
    
    if not (isinstance(student[0], str) and isinstance(student[1], str) and isinstance(student[2], float)): #проверяем, что именно 1-фио, 2-группа,3-GPA.
        return "TypeError"

    fio_parts = student[0].split() # Разделяем ФИО на части
    
    if len(fio_parts) < 2:
        return "ValueError: ФИО должно содержать фамилию и имя"
    
    # Очищаем от лишних пробелов и формируем фамилию и имя
    fio_parts = [part.strip() for part in fio_parts if part.strip()]
    
    res = fio_parts[0].title() + " " + fio_parts[1][0].upper() # Формируем фамилию и первую букву имени с большой буквы
    
    # Добавляем инициалы отчества, если оно есть
    if len(fio_parts) == 3:
        res += "." + fio_parts[2][0].upper() + "., "  
        res += "., "  

    res += "гр. " + student[1] + ", GPA " + f"{round(student[2],2):.2f}" #соединяем все в одно и округляем
    return res 

print(format_record(("Иванов Иван Иванович","BIVT-25",4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("Иванов Иван Иванович","BIVT-25", 4.5)))
</code></pre>  
<<img width="686" height="469" alt="image" src="https://github.com/user-attachments/assets/2c75c151-08c8-45b4-91a4-31243f53bcff" />
>


  

  
  





  



  
  






