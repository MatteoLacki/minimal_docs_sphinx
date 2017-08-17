import numpy as np
from pyteomics import mzxml


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


def stupid_function():
    """A stupid function.

    Returns
	-------
	out : list
        Returns an empty list.
    """
    return []


def get_mzxml(path, prec_digits=2):
    """Generate a sequence of rounded and trimmed spectra from individual runs of the instrument.

    Parameters
    ----------
    path : str
        Path to the mzXml file containing the mass spectrum.
    prec_digits : float
        The number of digits after which the floats get rounded.

    Returns
    -------
    out : generator
        Generates tuples of numpy arrays corresponding to different runs of the experimental spectrum.
    """
    with mzxml.read(path) as reader:
        for spectrum in reader:
            mz = spectrum['m/z array']
            intensity = spectrum['intensity array']
            mz, intensity = round_spec(mz, intensity, prec_digits)
            yield mz, intensity
