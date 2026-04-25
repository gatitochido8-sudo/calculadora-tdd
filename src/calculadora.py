# test suma
def suma(a, b):
    return a + b

# test resta
def resta(a, b):
    return a - b

# test multiplicacion
def multiplicacion(a, b):
    return a * b

# test division
def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

# test raiz cuadrada
def raiz_cuadrada(x, tolerancia=1e-3):
    if x < 0:
        raise ValueError("No existe raíz de número negativo")

    estimacion = x
    while True:
        nueva = 0.5 * (estimacion + x / estimacion)
        if abs(nueva - estimacion) < tolerancia:
            return nueva
        estimacion = nueva

# test exponencial
def exponencial(x, tolerancia=1e-3):
    resultado = 1
    termino = 1
    n = 1

    while abs(termino) > tolerancia:
        termino *= x / n
        resultado += termino
        n += 1

    return resultado
    fix: corrección de funciones y estructura del código
