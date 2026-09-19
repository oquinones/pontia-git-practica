def info():
    return "Operaciones básicas"


def suma(a: int, b: int):
    return a + b
    

if __name__ == "__main__":
    print(info())
    print(f"Suma de 3 y 4 = {suma(3, 4)}")