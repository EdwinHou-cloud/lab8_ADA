#Original
"""def ANALISIS(arr, target):
    n = len(arr)
    triplets = []
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == partida:
                    triplets.append((arr[i], arr[j], arr[k]))
    return triplets

#ejemplo de uso
arr = [1,2,3,4,5]
partida = 9
print(ANALISIS(arr, partida))"""

#Modificación
def ANALISIS(arr, target):
    n = len(arr)
    triplets = []
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == partida:
                    triplets.append((arr[i], arr[j], arr[k]))
    return triplets

# Ejemplo de uso
arr = [1, 2, 3, 4, 5]
# Solicitar al usuario que ingrese el tope
partida = int(input("Ingrese el valor del tope: "))
result = ANALISIS(arr, partida)

# Mostrar el resultado
print(f"Tripletas que suman a {partida}: {result}")
