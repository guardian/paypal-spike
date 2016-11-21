# ----- Imports ----- #

from urllib.parse import urlencode
from flask import Flask, render_template, redirect
import paypal


# ----- Setup ----- #

PAYPAL_URL = 'https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token={}'

app = Flask(__name__)


# ----- Routes ----- #

@app.route('/')
def checkout():

	return render_template('checkout.html')

@app.route('/paypal')
def auth_payment():

	token = paypal.setup_payment()
	redirect_url = PAYPAL_URL.format(token)

	return redirect(redirect_url)


# ----- Run ----- #

if __name__ == "__main__":
    app.run(debug=True)
