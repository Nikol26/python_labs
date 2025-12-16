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
