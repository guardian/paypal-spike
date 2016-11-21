# ----- Imports ----- #

from flask import Flask


# ----- Setup ----- #

app = Flask(__name__)


# ----- Routes ----- #

@app.route('/')
def checkout():

	return 'Checkout'


# ----- Run ----- #

if __name__ == "__main__":
    app.run()
