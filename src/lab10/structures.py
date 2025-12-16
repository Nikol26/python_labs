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
