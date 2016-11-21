# ----- Imports ----- #

from flask import Flask, render_template


# ----- Setup ----- #

app = Flask(__name__)


# ----- Routes ----- #

@app.route('/')
def checkout():

	return render_template('checkout.html')

@app.route('/paypal')
def paypal():

	return 'The paypal page.'


# ----- Run ----- #

if __name__ == "__main__":
    app.run(debug=True)
