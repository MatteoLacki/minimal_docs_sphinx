import numpy as np

def test_fun(x):
	"""A test function

	Parameters
	----------
		x : int
			An int.
	Returns
	-------
		x : int
			The same fucking int.
	Notes
	-----
	This is soo stupid.

	Warning
	-------
		Don't do it at home!!!

	Example
	-------
		>>> test_fun(10)
		10
	"""
	print('This is x:', x)
	return x

def test_fun_np():
    """A test function with numpy.

    Returns
	-------
	out : array
		An array of zeros.
    """
    return p.zeros(100)
