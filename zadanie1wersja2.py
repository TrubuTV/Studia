numbers=[]
nuuumbers=[]
p=int(input("Podaj system 2-10: "))
hm=int(input("Jak wielka bedzie ta liczba? "))



for a in range(hm):
    c=int(input("Podaj cyfre ktora ma byc zmieniona"))
    nuuumbers.append(c)

print(nuuumbers)


for i in nuuumbers:
    print(f"Tu jest I {i}")
    liczba=(i*pow(p,hm-1))
    numbers.append(liczba)
    
print(sum(numbers))
hm=hm-1
    
