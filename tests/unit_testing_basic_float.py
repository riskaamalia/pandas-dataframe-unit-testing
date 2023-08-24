import unittest
import pandas

'''
A unit testing of pandas dataframe data quality in float data type
'''


class DFFloatTests(unittest.TestCase):

    """ class for running unittests of float data type
            Args:
                    data (pd.DataFrame): data
                    column_names: list"""

    def input_dataframe(self):
        data = [{'Geeks': 23, 'For': 23.4, 'geeks': 123},
                {'Geeks': 10, 'For': 20, 'geeks': 30}]
        test_data = pandas.DataFrame.from_records(data)

        return test_data

    # this is a mandatory function
    # checking parameter is a pandas Dataframe or not
    def test_is_dataframe(self):
        # call the module here, call from facade pattern (main)
        test_data = self.input_dataframe()

        return self.assertEqual(True, isinstance(test_data, pandas.DataFrame))

    # this is a mandatory function
    # checking parameter is empty dataframe or not
    def test_is_empty_dataframe(self):
        test_data = self.input_dataframe()

        is_empty = test_data.empty
        if is_empty is False:
            if len(test_data.index) < 1:
                is_empty = True
        # return your equal result here
        return self.assertEqual(False, is_empty)

    # checking is dataframe, row or column is float datatype
    def test_is_float_datatype(self):
        test_data = self.input_dataframe()
        # check float data type in columns
        data_type = str(test_data.For.dtype)
        # check float data type in all
        # print(test_data.dtypes)

        # check float data type in cell
        return self.assertEqual('float64', data_type)

    def test_float_range(self):
        # testing float in a range of x and y of a parameter
        # call the function here
        # test_data = self.input_dataframe()
        # start_range = 12
        # end_range = 34
        self.assertEqual(4, 4)

    def test_float_less(self):
        # testing float is less of a parameter

        return False

    def test_float_less_than(self):
        # testing float is less than of a parameter

        return False

    def test_float_greater(self):
        # testing float is greater of a parameter

        return False

    def test_float_greater_than(self):
        # testing float is greater than of a parameter

        return False

    def test_float_is_in(self):
        # ini apa bedanya sama range?
        return False

    def test_float_length_after_comma(self):
        # testing total number after comma

        return False


if __name__ == '__main__':
    unittest.main()
