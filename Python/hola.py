import math

# Funcion para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2 
    return area

# Ejemplo de uso
radio = 5 # Radio del círculo 
area = calcular_area_circulo(radio)
print(f"El área de un círculo con radio {radio} es:  {area:.2f}")
