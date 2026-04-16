import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    print('test_add PASSED')

def test_subtract():
    assert calculator.subtract(10, 3) == 7
    print('test_subtract PASSED')

def test_multiply():
    assert calculator.multiply(3, 4) == 12
    print('test_multiply PASSED')

def test_divide():
    assert calculator.divide(10, 2) == 5.0
    print('test_divide PASSED')

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    print("All tests PASSED!")