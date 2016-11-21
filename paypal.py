# ----- Imports ----- #

from urllib.parse import parse_qs
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

	return {**REQUEST_DEFAULTS, **data}


def setup_payment():

	"""Sets up the payment authorization, returns the token."""

	req_data = {
		'METHOD': 'SetExpressCheckout',
		'PAYMENTREQUEST_0_PAYMENTACTION': 'SALE',
		'PAYMENTREQUEST_0_AMT': '4.20',
		'PAYMENTREQUEST_0_CURRENCYCODE': 'GBP',
		'RETURNURL': 'http://localhost:9000/',
		'CANCELURL': 'http://localhost:9000/',
		'BILLINGTYPE': 'MerchantInitiatedBilling'
	}

	r = requests.post(ENPOINT_URL, data=build_data(req_data))
	response_data = parse_qs(r.text)

	return response_data['TOKEN']
