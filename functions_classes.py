class Functions: 

    """

    Functions class has attributes of sum, a max and min tuple, and max difference

    """

    def __init__(self, num_list):

        """

        Initialized the attributes of the class Functions

        """

        self.num_list = num_list
        self.find_sum = find_sum
        self.find_min_max = find_min_max
        self.find_max_diff = find_max_diff

    import logging
    logging.basicConfig(filename = 'logging.txt', format = '%(asctime)s %(message)s', datefmt = '%m/%d/%Y &I:%M:%S %p', level = logging.DEBUG)

    def find_sum(num_list):

        """

        sum functions takes a list of numbers and returns a sum

        :param num_list: list of numbers
        :returns list_sum :sum of list of numbers

        """
        import numpy as np
        list_sum = np.sum(num_list)

        return  list_sum

    def find_max_diff(num_list):

        """

        function takes a list of integers and returns the max difference between two adjacent
        numbers

        :param num_list: list of numbers
        :returns max_diff: maximum difference

        """

        import numpy as np
        diff = np.diff(num_list)
        maxdiff = diff.max()

        return maxdiff

    def find_min_max(num_list):

        """

        Function takes a list of numbers and returns min and max in a tuple

        :param num_list: list of numbers
        :returns min_max: a tuple containing the max and the min

        """
        import numpy as np
        min_list = np.min(num_list)
        max_list = np.max(num_list)
        min_max = (min_list, max_list)

        return min_max

    def find_exceptions():
        """

        function checks and raises appropriate excpetions: type, value, import

        :param num_list: list of numbers
        :raises TypeError: checks to make sure only integers are in the list of numbers
        :raises ImportError: checks to make sure the correct files are imported
        :raises ValueError: make sure the integers have real values

        """

        try:
            find_sum([num_list])
            find_max_diff([num_list])
            find_min_max([num_list])

        except TypeError:
            logging.debug('DEBUG: Check the data type in the list of numbers')
            logging.warning('WARNING: You have the wrong data type, be careful')
            raise TypeError

        except ImportError:
            logging.debug('DEBUG:Error in the imported file')
            logging.warning('WARNING: File DNE')
            raise ImportError

        except ValueError:
            logging.debug('DEBUG: value error, check the list of numbers')
            logging.warning('WARNING: value error, value other than an integer is an input')
            raise ValueError

    def main(num_list):
        import logging
        logging.info('INFO: Program started')
        find_exceptions(num_list)
        sum_  = find_sum(num_list)
        max_min = find_min_max(num_list)
        max_diff = find_max_diff(num_list)
        logging.info('INFO:Program ended')

        return sum_, max_min, max_diff

