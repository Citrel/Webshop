import mollie.api.client as mollie
import os

class MolliePayment:
    def __init__(self, amount, description, redirect_url):
        self.amount = amount
        self.description = description
        self.redirect_url = redirect_url
        # TODO Mollie Test API Key ersetzen
        self.api_key = os.getenv('test_TjccvBdvN96qztsGp7U3mRB5QmjVHn') 
        self.mollie_client = mollie.Client()
        self.mollie_client.set_api_key(self.api_key)
        
    def create_payment(self):
        payment = self.mollie_client.payments.create({
            "amount": {
                "currency": "EUR",
                "value": str(self.amount)
            },
            "description": self.description,
            "redirectUrl": self.redirect_url,
            "method": "paypal"
        })
        return payment
    
    def get_payment(self, payment_id):
        payment = self.mollie_client.payments.get(payment_id)
        return payment
        
    def process_payment(self, payment_id, payment_token):
        payment = self.get_payment(payment_id)
        if payment.is_paid():
            return True
        elif payment.is_canceled():
            return False
        else:
            payment_status = payment.status
            if payment_status == "open":
                payment = payment.pay({"paymentToken": payment_token})
                return payment.is_paid()
            else:
                return False
