import numpy as np 
import pandas as pd
import pytest
from mock import MagicMock, patch


from lib import dataframe_helpers


data = {
					"a": [0, 1, 2, 3, 2, 1, 3, 0, 3], # sum = 15  
					"b": [0, 0, 0, 0, 0, 0, 0, 0, 0], # sum =  0
					"c": [2, 1, 2, 3, 1, 3, 2, 3, 3], # sum = 20 
					"d": [1, 0, 0, 1, 0, 1, 1, 0, 1]  # sum =  5
				}
dataframe = pd.DataFrame(data= data)
threshold = 0.1


class TestRemoveLowVariance:
	"""
	This class tests the remove low variance function
	""" 



	def test_remove_low_variance(self): 
		"""
		This function tests 'remove_low_var' with ideal parameters.
		"""
		

		expected_output_columns = ['a','c','d']
		expected_output = dataframe[ expected_output_columns ]

		actual_output = dataframe_helpers.remove_low_variance(dataframe, threshold)

		pd.testing.assert_frame_equal(expected_output, actual_output)
		

	def test_remove_low_variance_throws_error(self):
		"""
		This test asserts that remove_low_var throws an error
		when there exist no columns within the low variance dataframe
		"""

		data_all_zero = {
			"a": [ 0, 0, 0, 0, 0],
			"b": [ 0, 0, 0, 0, 0],
			"c": [ 0, 0, 0, 0, 0],
			"d": [ 0, 0, 0, 0, 0]
		}

		dataframe_no_var = pd.DataFrame(data=data_all_zero)


		with pytest.raises(RuntimeError, match="remove_low_variance removed all features from dataframe."):
			dataframe_helpers.remove_low_variance(dataframe_no_var, threshold)


class TestRemoveLowVarianceAndWriteToFile: 
	"""
	This test class tests the remove_low_variance_and_write_to_file function. 
	"""

	def test_remove_low_variance_and_write_to_file(self, mocker):
		"""
		This function tests remove_low_variance_and_write_to_file. 
		"""
		
		output_file = "testout.tsv"

		rlv_mock = mocker.patch("lib.dataframe_helpers.remove_low_variance", return_value=dataframe)
		to_csv_mock = mocker.patch.object(dataframe, "to_csv")
		
		dataframe_helpers.remove_low_variance_and_write_to_file(dataframe, threshold, output_file)

		rlv_mock.assert_called_once_with(dataframe, threshold)
		to_csv_mock.assert_called_once_with(output_file)
