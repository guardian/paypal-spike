# ----- Imports ----- #

from urllib.parse import urlencode
from flask import Flask, render_template, json, request
import paypal


# ----- Setup ----- #

PAYPAL_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token={}'

app = Flask(__name__)


# ----- Routes ----- #

@app.route('/')
def checkout():

	return render_template('checkout.html')


@app.route('/paypal', methods=['POST'])
def auth_payment():

	token = paypal.setup_payment(
		return_url='http://localhost:5000/create_payment',
		cancel_url='http://localhost:5000/cancel'
	)

	# redirect_url = PAYPAL_URL.format(token)

	return json.dumps({'token': token})


@app.route('/create_payment')
def create_payment():

	token = request.args.get('token')
	baid = paypal.create_agreement(token)

	return render_template('baid.html', baid=baid)


@app.route('/cancel')
def cancel():

	return 'An error!'


# ----- Run ----- #

if __name__ == "__main__":
    app.run(debug=True)
