# ----- Imports ----- #

from urllib.parse import parse_qs
import requests
import os


# ----- Setup ----- #

ENPOINT_URL = 'https://api-3t.sandbox.paypal.com/nvp'

REQUEST_DEFAULTS = {
	'USER': os.environ['PAYPAL_SPIKE_USER'],
	'PWD': os.environ['PAYPAL_SPIKE_PWD'],
	'SIGNATURE': os.environ['PAYPAL_SPIKE_SIG'],
	'VERSION': '124.0'
}


# ----- Functions ----- #

def build_data(data):

	"""Formats the data to be sent in a request, adds required defaults."""

	return {**REQUEST_DEFAULTS, **data}


def setup_payment(return_url, cancel_url):

	"""Sets up the payment authorization, returns the token."""

	req_data = {
		'METHOD': 'SetExpressCheckout',
		'PAYMENTREQUEST_0_PAYMENTACTION': 'SALE',
		'PAYMENTREQUEST_0_AMT': '4.20',
		'PAYMENTREQUEST_0_CURRENCYCODE': 'GBP',
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
