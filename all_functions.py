
def sum_list(num_list):
    sum_ = sum(num_list)
    return sum_


def find_min(number_list):
    import numpy as np
    min_ = np.min(number_list)
    return min_


def find_max(number_list):
    import numpy as np
    max_ = np.max(number_list)
    return max_


def tuple_generator(min_, max_):
    min_max = (min_, max_)
    return min_max


def maxdiff(input):
    import numpy as np
    diff = np.diff(input)
    maxdiff = diff.max()
    return maxdiff
