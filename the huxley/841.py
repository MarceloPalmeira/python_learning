
x = float(input())
y = float(input())
z = float(input())

media = (x + y + z)/3

qt = 0

if x > media:
    qt += 1

if y > media:
    qt += 1

if z > media:
    qt += 1

print (qt)