# Paypal Spike

The spike for testing Paypal integration with the membership checkout. Demo server written in Python (3.5).

## To Install

Install:

```
pip install -r requirements.txt
```

## To Run

Set the `PAYPAL_SPIKE_USER`, `PAYPAL_SPIKE_PWD` and `PAYPAL_SPIKE_SIG` environment variables, e.g.:

```
export PAYPAL_SPIKE_USER='my_user@my_domain.com'
```

Serve:

```
python server.py
```

View:

```
http://localhost:5000
```

and use a buyer test user.
