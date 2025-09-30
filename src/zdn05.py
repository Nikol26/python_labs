f=input("ФИО: ")
n=f.split()
f=f.replace(' ','')
i=n[0][:1]+n[1][:1]+n[2][:1]+'.'
print(f'Инициалы:{i}')
print(f'Длина (символов){len(f)+2}')