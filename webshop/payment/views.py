from django.shortcuts import render, redirect
from .mollie import MolliePayment

class Payment:
    def process_payment(request):
        if request.method == 'POST':
            amount = request.POST['amount']
            description = request.POST['description']
            redirect_url = request.POST['redirect_url']
            
            mollie_payment = MolliePayment(amount, description, redirect_url)
            payment = mollie_payment.create_payment()
            
            request.session['payment_id'] = payment.id
            
            return redirect(payment.checkout_url)
        else:
            return render(request, 'payment_form.html')
