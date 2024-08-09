
def add(x: int, y: int) -> int:
    """ returns x + y"""
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError
    return x + y

def add_sales_tax(x: int) -> float:
    return round(x * 1.06, 2)

def is_negative():
    pass

if __name__ == "__main__":
    print(add(5, 3))