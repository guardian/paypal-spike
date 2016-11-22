# ----- Imports ----- #

from urllib.parse import urlencode
from flask import Flask, render_template, json, request
import paypal


# ----- Setup ----- #

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

	return json.jsonify({'token': token})


@app.route('/create_payment', methods=['POST'])
def create_payment():

	token = request.get_json()['token']
	baid = paypal.create_agreement(token)

	return json.jsonify({'baid': baid})


@app.route('/cancel')
def cancel():

	return 'An error!'


# ----- Run ----- #

if __name__ == "__main__":
    app.run(debug=True)
