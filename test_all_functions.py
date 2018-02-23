from functions_classes import Functions
import pytest

class TestFunctions(pytest):

     def  test
    import pytest
    import math

    list_of_numbers_1 = [29, 3, 77, 55]
    list_of_numbers_2 = [1.23, 9, 6.97, 7, 27.01]
    list_of_numbers_3 = [-7, -8, 26, 54, -2]


    def test_max_diff(self):
       from functions_classes import Functions
   #   from Functions import find_max_diff
       maxdiff_outputf = maxdiff([1,2,4,7])
       assert maxdiff_output == 3


    def test_sum_list_integer(self):
      from Functions import find_sum
      sum_ = sum_list(list_of_numbers_1)
      assert sum_ == 164


    def test_sum_list_decimals(self):
         from Functions import find_sum
         sum_ = sum_list(list_of_numbers_2)
         assert sum_ == 51.21


    def test_sum_list_negative(self):
       from Functions import find_sum
       sum_ = sum_list(list_of_numbers_3)
       assert sum_ == 63


    def test_min(self):
       from Functions import find_min_max
       min_ = find_min_max([4, 7,-20])
       assert min_[0] == -20


    def test_max(self):
       from Functions import find_min_max
       max_ = find_min_max([1010, 32 -302931])
       assert max_[1] == 1010


    def test_precision(self):
       from Functions import find_min_max
       max_ = find_min_max([1.33, 0, -222])
       assert max_ == (-222, 1.33)


    def test_tuple_size(self):
       from Functions import find_min_max
       min_max = find_min_max([23, 53,123123123, -13934])
       assert len(min_max) == 2

    def test_try_exception_type(self):
       from Functions import find_exceptions
       with pytest.raises(TypeError):
          find_exceptions(['a', 7, -20])

    def test_try_exception_import(self):
        from Functions import find_exceptions
        with pytest.raises(ImportError):
            import ThisIsNotAFile

    def test_try_exception_value(self):
        from Functions import find_exceptions
        with pytest.raises(ValueError):
             find_exceptions([math.sqrt(-12421412), 23232, -12412])
