# test_app.py
# Basit pytest örnekleri

def add(a, b):
    """Toplama fonksiyonu (örnek amaçlı)."""
    return a + b

def multiply(a, b):
    """Çarpma fonksiyonu (örnek amaçlı)."""
    return a * b


# ✅ Testler

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 99) == 0

def test_combined_operations():
    result = multiply(add(2, 3), 2)  # (2+3)*2 = 10
    assert result == 10
