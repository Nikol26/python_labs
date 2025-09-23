f=input("ФИО: ")
n=f.split()
i=n[0][:1]+n[1][:1]+n[2][:1]+'.'
print(i)
print(len(f.replace('  ',' ')))