def add(a1,a2):
    return a1+a2
def sub(a1,a2):
    return a1-a2
def mul(a1,a2):
    return a1*a2
def div(a1,a2):
    return a1/a2

def calculartor(a1,a2,fun):
    return fun(a1,a2)
print(calculartor(1,2,add))
