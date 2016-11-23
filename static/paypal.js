paypal.Button.render({
				
	env: 'sandbox', // Specify 'production' for the prod environment

	// Called when user clicks Paypal button.
	payment: function (resolve, reject) {

		const CREATE_PAYMENT_URL = '/paypal';

		paypal.request.post(CREATE_PAYMENT_URL)
			.then(data => {
				resolve(data.token);
			})
			.catch(err => {
				reject(err);
			});

	},

	// Called when user finishes with Paypal interface (approves payment).
	onAuthorize: function (data, actions) {

		const CREATE_AGREEMENT_URL = '/create_payment';

		fetch(CREATE_AGREEMENT_URL, {
			headers: { 'Content-Type': 'application/json' },
			method: 'POST',
			body: JSON.stringify({ token: data.paymentToken })
		}).then(response => {
			return response.json();
		}).then(baid_data => {
			alert(`Your BAID: ${baid_data.baid}`);
		}).catch(err => {
			alert('Uh oh!');
		});

   }
		
}, '#paypal-button');
