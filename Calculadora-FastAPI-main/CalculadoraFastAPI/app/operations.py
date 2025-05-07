def add(a:float, b:float) -> float:
    return a + b

def subtract(a:float, b:float) -> float:
    return a - b

def multiply(a:float, b:float) -> float:
    return a * b

def divide(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def exponentiation(a:float, b:float) -> float:
    return a ** b

def rooting(a:float, b:float) -> float:
    if b == 0:
        raise ValueError("Root degree cannot be zero")
    return a ** (1 / b)