import pytest

from main import add, add_sales_tax


def test_add():
    assert add(5, 5) == 10
    
def test_add_throws_error_on_characters():
    with pytest.raises(ValueError) as e_info:
        print(add('x', 'à'))
        
def test_add_throws_error_on_float():
    with pytest.raises(ValueError) as e_info:
        print(add(4.56567, 1.23))
        
        
def test_add_and_sales_tax():
    total = add(5, 5)
    withTax = add_sales_tax(total)
    assert withTax == 10.6
        
        
def test_add_sales_tax():
    assert add_sales_tax(1) == 1.06