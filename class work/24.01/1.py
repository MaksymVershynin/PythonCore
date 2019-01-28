def triad(a,b):
    return a*b/2
def rectangle(a,b):
    return a*b
def circle(r):
    return 3.14*r*r
choise=int(input('choise:\n1-triad\n2-rectangle\n3-circle\n'))
if choise==1:
    a=int(input("a = "))
    b=int(input('b = '))
    s=triad(a,b)
elif choise == 2:
    a=int(input("a = "))
    b=int(input('b = '))
    s=rectangle(a,b)
elif choise == 3:
    r=int(input('r ='))
    s=circle(r)
else: print('no')

print('s ={}'.format(s))