import numpy as np
import logging

logging.basicConfig(filename='logging.txt', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y &I:%M:%S %p', level=logging.DEBUG)


def sum_list(num_list):

    """Function takes list of integers and returns the sum of the list

       :param num_list: list of integers
       :returns sum_: the sum of the list of integers

       """

    sum_ = sum(num_list)

    return sum_


def find_min_max(num_list):
    """Function takes list of integers and returns min and max in a tuple

    :param num_list: list of integers
    :returns max_min: a tuple containing the max and min of a list

    """ 
    min_ = np.min(num_list)
    max_ = np.max(num_list)
    max_min = (min_, max_)

    return max_min


def maxdiff(num_list):
    """Function takes a list of integers and returns the maximum difference between two adjacent numbers

    :param num_list: list of integers
    :returns maxdiff: maximum difference 
    """

    diff = np.diff(num_list)
    maxdiff = diff.max()

    return maxdiff


def find_exceptions(num_list):

    """ fxn checks and raises appropriate exceptions: type, value and import

    :param num_list: list of integers
    :raises TypeError: checks to make sure list is integers
    :raises ImportError: checks to make sure correct files are imported
    :raises ValueError: makes sure the integers have real values

    """
    try:
        find_min_max([num_list])
        maxdiff([num_list])
        sum_list([num_list])
    except TypeError:
        logging.debug('DEBUG: Try checking the data type of number_list')
        logging.warning('WARNING: Your Program may blow up from the wrong data type')
        raise TypeError

    except ImportError:
        logging.debug('DEBUG: Error in input files')
        logging.warning('WARNING: You have tried to import something that DNE')
        raise ImportError

    except ValueError:
        logging.debug('DEBUG: There is a value error, make sure the integer is real')
        logging.warning('Warning: there is a value error, make sure the integer is real')
        raise ValueError
