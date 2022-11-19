numbers=[]
p=int(input("Podaj system 2-10: "))
c=int(input("Ilu znakowa bedzie liczba?"))

while c>0:
  b=int(input("Podaj pozycje cyfy: "))
  a=int(input("Podaj liczbe: "))
  if a<p and b<p:
    liczbka = (a*pow(p,b-1))
    numbers.append(liczbka)
    print(sum(numbers))
    c=c-1
  else:
    print("Liczba wyszla poza system!")
    break
  



  
  