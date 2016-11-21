# ----- Imports ----- #

import requests


# ----- Setup ----- #

ENPOINT_URL = 'https://api-3t.sandbox.paypal.com/nvp'

REQUEST_DEFAULTS = {
	'USER': '***REMOVED***',
	'PWD': '***REMOVED***',
	'SIGNATURE': '***REMOVED***',
	'VERSION': '86.0'
}


# ----- Functions ----- #

def build_data(data):

	"""Formats the data to be sent in a request, adds required defaults."""

	return {REQUEST_DEFAULTS**, data**}



