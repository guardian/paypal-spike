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


def setup_payment(return_url, cancel_url):

	"""Sets up the payment authorization, returns the token."""

	req_data = {
		'METHOD': 'SetExpressCheckout',
		'RETURNURL': return_url,
		'CANCELURL': cancel_url,
		'BILLINGTYPE': 'MerchantInitiatedBilling'
	}

	r = requests.post(ENPOINT_URL, data=build_data(req_data))
	response_data = parse_qs(r.text)

	return response_data['TOKEN'][0]


def create_agreement(token):

	"""Creates a billing agreement and returns the BAID."""

	req_data = {
		'METHOD': 'CreateBillingAgreement',
		'TOKEN': token
	}

	r = requests.post(ENPOINT_URL, data=build_data(req_data))
	response_data = parse_qs(r.text)

	return response_data['BILLINGAGREEMENTID'][0]
