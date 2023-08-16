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

    # this is a mandatory function
    # fill column_names_checked if you want to check column
    # fill row_index_checked if you want to check row
    # default: all cells in dataframe is checked

    # this is a mandatory function
    # checking parameter is a pandas Dataframe or not
    def test_is_dataframe(self):
        # real result test in variable
        test_data = pandas.DataFrame()
        print(type(test_data))
        # call the module here
        return False

    # this is a mandatory function
    # checking parameter is empty dataframe or not
    def test_is_empty_dataframe(self):
        return False

    # this is a mandatory function
    # checking parameter is empty row dataframe or not
    def test_is_empty_dataframe_row(self):
        return False

    # this is a mandatory function
    # checking parameter is empty column dataframe or not
    def test_is_empty_dataframe_column(self):
        return False

    # checking is dataframe, row or column is float datatype
    def test_is_float_datatype(self):
        return False

    def test_range(self):
        self.assertEqual(4, 4)


if __name__ == '__main__':
    unittest().main()
