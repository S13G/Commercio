from decimal import Decimal
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

from orders.models import Order
from .tasks import payment_completed

# instantiate Braintree payment gateway


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()




def payment_done(request):
    return render(request, 'payment/done.html')


def payment_canceled(request):
    return render(request, 'payment/canceled.html')
