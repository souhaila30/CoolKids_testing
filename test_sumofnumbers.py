list_of_numbers_1 = [29, 3, 77, 55]
list_of_numbers_2 = [1.23, 9, 6.97, 7, 27.01]
list_of_numbers_3 = [-7, -8, 26, 54, -2]


def test_sum_list_integer():
    from sumofnumbers import sum_list
    sum_ = sum_list(list_of_numbers_1)
    assert sum_ == 164

def test_sum_list_decimals():
    from sumofnumbers import sum_list
    sum_ = sum_list(list_of_numbers_2)
    assert sum_ == 51.21

def test_sum_list_negative():
    from sumofnumbers import sum_list
    sum_ = sum_list(list_of_numbers_3)
    assert sum_ == 63
