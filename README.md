# ЛР10 — Структуры данных: Stack, Queue, Linked List и бенчмарки

# A. Реализовать Stack и Queue (src/lab10/structures.py)
```python
from collections import deque
from typing import Any, Optional


class Stack:
    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if not self._data:
            raise IndexError('pop from empty Stack')
        return self._data.pop()

    def peek(self) -> Optional[Any]:
        return self._data[-1] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        self._data.append(item)

    def dequeue(self) -> Any:
        if not self._data:
            raise IndexError('dequeue from empty Queue')
        return self._data.popleft()

    def peek(self) -> Optional[Any]:
        return self._data[0] if self._data else None

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


if __name__ == "__main__":
    print("Stack")

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(f"Снятие верхнего элемента стека : {stack.pop()}")
    print(f"Пустой ли стек? {stack.is_empty()}")
    print(f"Число сверху : {stack.peek()}")

    stack.push(1)
    print(f"Значение сверху после добавления числа в стек : {stack.peek()}")
    print(f"Длина стека : {len(stack)}")
    print(f"Стек : {stack._data}")

    print("Deque")

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(f"Значение первого элемента : {q.peek()}")
    q.dequeue()
    print(f"Значение первого элемента после удаления числа : {q.peek()}")

    q.enqueue(52)
    print(f"Значение первого элемента после добавления числа : {q.peek()}")
    print(f"Пустая ли очередь? {q.is_empty()}")
    print(f"Количество элементов в очереди : {len(q)}")
```

<img width="476" height="200" alt="ЛР 10 2" src="https://github.com/user-attachments/assets/0710f0e6-33df-42d2-b9ba-1d2bc1f78e7a" />

# B. Реализовать SinglyLinkedList (src/lab10/linked_list.py)
```python
from typing import Any, Iterator, Optional


class Node:
    def __init__(self, value: Any, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0

    def append(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self._size += 1

    def prepend(self, value: Any) -> None:
        node = Node(value, self.head)
        self.head = node
        if self._size == 0:
            self.tail = node
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError("index out of range")
        if idx == 0:
            self.prepend(value)
            return
        if idx == self._size:
            self.append(value)
            return

        prev = self.head
        for _ in range(idx - 1):
            prev = prev.next

        node = Node(value, prev.next)
        prev.next = node
        self._size += 1

    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError("index out of range")

        prev = None
        cur = self.head
        for _ in range(idx):
            prev, cur = cur, cur.next

        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next

        if cur is self.tail:
            self.tail = prev

        self._size -= 1

    def __iter__(self) -> Iterator[Any]:
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        parts = []
        cur = self.head
        while cur:
            parts.append(f"[{cur.value}]")
            cur = cur.next
        parts.append("None")
        return " -> ".join(parts)


if __name__ == "__main__":
    sll = SinglyLinkedList()

    print(f"Длина нашего односвязного списка : {len(sll)}")

    sll.append(1)
    sll.append(2)
    sll.prepend(0)

    print(f"Наша нынешняя длина списка после добавления элементов : {len(sll)}")
    print(f"Односвязанный список : {list(sll)}")

    sll.insert(1, 0.5)
    print(f"Длина списка после добавления на 1 индекс числа 0.5 : {len(sll)}")
    print(f"Односвязанный список : {list(sll)}")

    sll.append(52)
    print(f"Односвязанный список после добавления числа в конец : {list(sll)}")

    print(sll)
```
<img width="479" height="119" alt="ЛР 10 1" src="https://github.com/user-attachments/assets/eb148b0e-51ec-41a7-ae82-3b26854d3292" />

# Теория 
Стек (Stack)
Принцип: LIFO — Last In, First Out.

Операции:

push(x) — положить элемент сверху;
pop() — снять верхний элемент;
peek() — посмотреть верхний, не снимая.
Типичные применения:

история действий (undo/redo);
обход графа/дерева в глубину (DFS);
парсинг выражений, проверка скобок.
Асимптотика (при реализации на массиве / списке):

push — O(1) амортизированно;
pop — O(1);
peek — O(1);
проверка пустоты — O(1).
Очередь (Queue)
Принцип: FIFO — First In, First Out.

Операции:

enqueue(x) — добавить в конец;
dequeue() — взять элемент из начала;
peek() — посмотреть первый элемент, не удаляя.
Типичные применения:

обработка задач по очереди (job queue);
обход графа/дерева в ширину (BFS);
буферы (сетевые, файловые, очереди сообщений).
В Python:

обычный list плохо подходит для реализации очереди:
удаление с начала pop(0) — это O(n) (все элементы сдвигаются);
collections.deque даёт O(1) операции по краям:
append / appendleft — O(1);
pop / popleft — O(1).
Асимптотика (на нормальной очереди):

enqueue — O(1);
dequeue — O(1);
peek — O(1).
Односвязный список (Singly Linked List)
Структура:

состоит из узлов Node;
каждый узел хранит:
value — значение элемента;
next — ссылку на следующий узел или None (если это последний).
Основные идеи:

элементы не хранятся подряд в памяти, как в массиве;
каждый элемент знает только «следующего соседа».
Плюсы:

вставка/удаление в начало списка за O(1):
если есть ссылка на голову (head), достаточно перенаправить одну ссылку;
при удалении из середины не нужно сдвигать остальные элементы:
достаточно обновить ссылки узлов;
удобно использовать как базовый строительный блок для других структур (например, для очередей, стеков, хеш-таблиц с цепочками).
Минусы:

доступ по индексу i — O(n):
чтобы добраться до позиции i, нужно пройти i шагов от головы;
нет быстрого доступа к предыдущему элементу:
чтобы удалить узел, нужно знать его предыдущий узел → часто нужен дополнительный проход.
Типичные оценки:

prepend (добавить в начало) — O(1);
append:
при наличии tail — O(1),
без tail — O(n), т.к. требуется пройти до конца;
поиск по значению — O(n).
Двусвязный список (Doubly Linked List)
Структура:

также состоит из узлов DNode;
каждый узел хранит:
value — значение элемента;
next — ссылку на следующий узел;
prev — ссылку на предыдущий узел.
Основные идеи:

можно двигаться как вперёд, так и назад по цепочке узлов;
удобно хранить ссылки на оба конца: head и tail.
Плюсы по сравнению с односвязным:

удаление узла по ссылке на него — O(1):
достаточно «вытащить» его, перенастроив prev.next и next.prev;
не нужно искать предыдущий узел линейным проходом;
эффективен для структур, где часто нужно удалять/добавлять элементы в середине, имея на них прямые ссылки (например, реализация LRU-кэша);
можно легко идти в обе стороны:
прямой и обратный обход списка.
Минусы:

узел занимает больше памяти:
нужно хранить две ссылки (prev, next);
код более сложный:
легко забыть обновить одну из ссылок и «сломать» структуру;
сложнее отлаживать.
Типичные оценки (при наличии head и tail):

вставка/удаление в начале/конце — O(1);
вставка/удаление по ссылке на узел — O(1);
доступ по индексу — O(n) (нужно идти от головы или хвоста);
поиск по значению — O(n).
Пример текстовой визуализации:

None <- [A] <-> [B] <-> [C] -> None




