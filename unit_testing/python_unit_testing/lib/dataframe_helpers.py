import pandas as pd

def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
	"""
	This function removes the low variance values from a dataframe
	determined by some threshold
	"""
	
	# Create mask and extract desired columns
	high_variance_mask = df.var() > threshold
	high_variance_columns = df.columns[high_variance_mask]

	# Extract desired columns from actual dataframe
	low_variance_dataframe = df[ high_variance_columns ] 

	if len(low_variance_dataframe.columns) == 0: 
		raise RuntimeError("remove_low_variance removed all features from dataframe.")
	return low_variance_dataframe


def remove_low_variance_and_write_to_file(df: pd.DataFrame, threshold: float, outfile: str) -> None: 
	"""
	This function calls remove_variance and saves the output to file. 
	"""

	low_variance_df = remove_low_variance(df, threshold)
	low_variance_df.to_csv(outfile)

	return None