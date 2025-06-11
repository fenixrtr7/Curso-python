def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mult(a, b):
    return a * b

def divi(a, b):
    if b == 0:
        raise ValueError(" No se puede dividir entre 0")
    return a / b

if __name__ == "__main__":
    print('Operaciones')
    res_1 = add(3,4)
    print(f'Suma: {res_1}')

