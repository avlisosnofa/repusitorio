'''
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))

graus = int(input("quantos graus fahr estão?"))
celsos = fahr_to_celsius(graus)
print(f'estão {celsos}ºC')
'''
a = 10
'''
def f1():

    r = a +a
    print(r)
def f2():
    r = a * a
    print(r)
 

f1()
f2()
'''
def f3():
    global a
    a = a * a
    print(a)