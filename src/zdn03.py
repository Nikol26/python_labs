from typing import Tuple

StudentRecord = Tuple[str, str, float]

def format_record(rec: StudentRecord) -> str:
    fio, group, gpa = rec
    fio_parts = [part.strip() for part in fio.split()]
    formatted_surname = fio_parts[0].capitalize()
    initials = ''.join([f'{name[0].upper()}.' for name in fio_parts[1:]])
    formatted_gpa = f'{gpa:.2f}'
    formatted_record = f"{formatted_surname} {initials}, гр. {group}, GPA {formatted_gpa}"
    return formatted_record
a = ("Иванов Иван Иванович","BIVT-25",4.6)
b = ("Петров Пётр", "IKBO-12", 5.0)
c = ("Петров Пётр Петрович", "IKBO-12", 5.0)
d = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
e = ("Иванов Иван Иванович","BIVT-25")
print(format_record(a))
print(format_record(b))
print(format_record(c))
print(format_record(d))
print(format_record(e))