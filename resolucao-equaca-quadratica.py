from time import sleep

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
d = (b)**2 - 4 * a * c
Xv = - (b) / (2*a)
Yv = - (d) / (4*a)
conc = a
if a != 0 and b != 0 and c != 0:
    d = (b)**2 - 4 * a * c
    print(f"DELTA = {d}")
    xx1 = -b - (d**0.5)
    xx2 = -b + (d**0.5)
    x1 = xx1/(2*a)
    x2 = xx2/(2*a)
    print(f"X1 = {x1:.1f} V X2 = {x2:.1f}")
    if x1 == x2:
        print("(ZERO DUPLOS)")

elif a != 0 and b != 0 and c == 0:
    if a < b:
        x1 = c
        x2 = -b
        print(f"X1 = {x1} V X2 = {x2}")
    elif a > b:
        x1 = -b
        x2 = c
        print(f"X1 = {x1} V X2 = {x2}")
    elif a == b:
        x1 = c
        x2 = -b
        print(f"X1 = {x1} V X2 = {x2}")

elif a != 0 and b == 0 and c != 0:
    x = c/a
    x1 = - (x**0.5)
    x2 = x ** 0.5
    print(f"X1 = {x1:.2f} V X2 = {x2:.2f}")

if conc > 0:
    print("CONCAVIDADE: Voltada para cima")
elif conc < 0:
    print("CONCAVIDADE: Voltada para baixo")
    
print(f"V({Xv};{Yv})")


    


    
          
    
