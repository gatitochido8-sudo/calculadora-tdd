from src.calculadora import *

def test_suma():
    assert suma(2, 3) == 5

def test_resta():
    assert resta(5, 2) == 3

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12

def test_division():
    assert division(10, 2) == 5

def test_division_cero():
    try:
        division(10, 0)
        assert False
    except ValueError:
        assert True

def test_raiz():
    assert abs(raiz_cuadrada(9) - 3) < 1e-3

def test_exponencial():
    assert abs(exponencial(1) - 2.718) < 1e-2
