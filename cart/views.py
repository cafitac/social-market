from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cart.models import Cart
from member.models import User


@login_required
def get_carts(request):
    request_user: User = request.user

    carts = Cart.objects.filter(user_id=request_user.id, is_deleted=False)

    cart_data = {"data": []}
    for cart in carts:
        cart_data['data'].append({
            "id": cart.id,
            "merchandise_name": cart.merchandise_name,
            "merchandise_price": cart.merchandise_price,
            "amount": cart.amount,
        })
    cart_data['total_price'] = sum([cart.merchandise_price * cart.amount for cart in carts])

    return render(request, 'cart/list.html', {
        'carts': cart_data,
    })
