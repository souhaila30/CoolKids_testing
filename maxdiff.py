def maxdiff(input):
	"""returns the max difference between two adjacent numbers"""
	import numpy as np
	diff = np.diff(input)
	maxdiff = diff.max()
	return maxdiff
		
	
