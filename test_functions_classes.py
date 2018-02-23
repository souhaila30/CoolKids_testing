from functions_classes import Functions
import pytest

def test_sum():
    test_sum = Functions.find_sum([1,2,3,4])
    assert test_sum == 10

def test_sum_decimals():
    test_sum = Functions.find_sum([1,2.5,3.5,4])
    assert test_sum == 11

def test_sum_negative():
    test_sum = Functions.find_sum([-1,2.5,3.5,-4])
    assert test_sum == 1

def test_min():
    test_min = Functions.find_min_max([4,2,0])
    assert test_min[0] == 0

def test_max():
    test_max = Functions.find_min_max([0,2,345,890])
    assert test_max[1] == 890

def test_precision():
    test_min_max = Functions.find_min_max([-3903,0.389,9870])
    assert test_min_max == (-3903, 9870)

def test_tuple_size():
    test_tuple = Functions.find_min_max([-3,0.3,8,29])
    assert len(test_tuple) == 2

def test_try_exception_type():
   # from functions_classes import find_exceptions
    with pytest.raises(TypeError):
        Functions.find_exceptions(['a',9,-1])

def test_try_exception_import():
   # from functions_classes import find_exceptions
    with pytest.raises(ImportError):
        import ThisIsNotAFile

def test_try_exception_value():
   # from functions_classes import find_exceptions
    with pytest.raises(ValueError):
       Functions.find_exceptions([56574564776846786])







