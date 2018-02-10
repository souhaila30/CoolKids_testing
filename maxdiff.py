def maxdiff(input):
	"""returns the max difference between two adjacent numbers"""
	import numpy as np
	input = [8,10,9,6]
	diff = np.diff(input)
	maxdiff = diff.max()
	return maxdiff
		
	
