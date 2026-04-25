def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def raiz_cuadrada(x, tolerancia=1e-3):
    if x < 0:
        raise ValueError("No existe raíz de número negativo")

    estimacion = x
    while True:
        nueva = 0.5 * (estimacion + x / estimacion)
        if abs(nueva - estimacion) < tolerancia:
            return nueva
        estimacion = nueva

def exponencial(x, tolerancia=1e-3):
    resultado = 1
    termino = 1
    n = 1

    while abs(termino) > tolerancia:
        termino *= x / n
        resultado += termino
        n += 1

    return resultado
