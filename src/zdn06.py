n=int(input())
ochno=[]
zaochno=[]
while n>0:
    fio=input()
    n=n-1
    if 'True' in fio:
        ochno.append(fio)
    elif 'Falce' in fio:
        zaochno.append(fio)
print(len(ochno),len(zaochno))

