# testing return max and min function

def test_min():
    from return_max_min import find_min
    min_ = find_min([4, 7,-20])
    assert min_ == -20

def test_max():
    from return_max_min import find_max
    max_ = find_max([1010, 32 -302931])
    assert max_ == 1010

def test_doubles():
    from return_max_min import find_max
    max_ = find_max([2, 2, 0])
    assert max_ == 2

def test_precision():
    from return_max_min import find_max
    max_ = find_max([1.33, 0, -222])
    assert max_ == 1.33

def test_tuple_size():
    from return_max_min import tuple_generator
    min_max = tuple_generator(23, 53)
    assert len(min_max) == 2

