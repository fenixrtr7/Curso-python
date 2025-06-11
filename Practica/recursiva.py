def sumatoria(n):
    if n == 0:
        return 0
    else:
        return sumatoria(n-1) + n
    
#print(sumatoria(10))

for i in range(110):
    print(f"Sumaoria de {i} es: {sumatoria(i)}")