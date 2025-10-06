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