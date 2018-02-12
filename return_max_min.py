
import numpy as np
import logging

logging.basicConfig(filename = 'logging.txt', format= '%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level =logging.DEBUG)

def find_min_max(number_list):
    """fxn takes list of integers and returns min and max in a tuple

    :param number_list: list of integers
    :raises TypeError: type error if string in list
    :returns max_min: a tuple containing the max and min of a list

    """
 
    try:
        min_ =np.min([number_list])
        max_ =np.max([number_list])
    except TypeError:
         logging.debug('DEBUG: Try checking the data type of number_list')
         logging.warning('WARNING: Your Program may blow up from the wrong data type')   
         raise TypeError #("you have the wrong Data type")
 
    else: 
        min_ = np.min(number_list)
        max_ = np.max(number_list)
        max_min = (min_, max_)
   
    return max_min


def main(number_list):
    logging.info('INFO: Program Started')
    max_min = find_min_max(number_list)
    logging.info('INFO: Program Ended')

    return max_min

