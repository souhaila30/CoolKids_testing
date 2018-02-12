# testing return max and min function
import pytest

def test_min():
    from return_max_min import find_min_max
    min_ = find_min_max([1312, -20, 12312])
    assert min_[0] == -20

def test_max():
    from return_max_min import find_min_max
    max_ = find_min_max([1010, 32 -302931])
    assert max_[1] == 1010

def test_precision():
    from return_max_min import find_min_max
    value = find_min_max([1.33, 0, -222])
    assert value == (-222, 1.33)

def test_tuple_size():
    from return_max_min import find_min_max
    min_max = find_min_max([23, 53, 234234, 12, -3929423])
    assert len(min_max) == 2

def test_try_exception_type():
    from return_max_min import find_min_max
    with pytest.raises(TypeError):
        find_min_max(['a',7,-20])
  

