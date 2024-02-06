"""
This module implements the main data analysis and visualisation functionality.

Author: Nicholas Holtzhausen
"""

import pandas as pd
import matplotlib as plt


class DataAnalysis:
	"""
	Class for the data analysis and data visualisation methods.

	Methods
	-------
	csv_to_df: method that reads csv file and returns df

	"""

	@staticmethod
	def csv_to_df(file_loc):
		"""
		Reads a CSV file and returns a pandas DataFrame containing the data.

		Parameters
		----------
		file_loc : str
			The file location of the CSV data

		Returns
		-------
		df : pd.DataFrame
			The original data represented as a dataframe
		"""

		df = pd.read_csv(file_loc)

		return df
