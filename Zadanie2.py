# Horner?

def horner(a,b,c):
    wynik=a[0]
    for n in range(1,b):
        wynik=wynik*c+a[1]
    return wynik


a=[2,-1,-6,3]
c=3
b=len(a)
print(f"Warosc tego wielomianu to {horner(a,b,c)}")