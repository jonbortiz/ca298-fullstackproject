from operator import truediv
from re import template
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from jonshop.forms import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


products = Product.objects.all()

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products':products})

def product_individual(request, prodid):
    # get the product with id = prodid
    product = Product.objects.get(id=prodid)
    return render(request, 'product_individual.html', {'product':product})

@login_required
def add_to_basket(request, prodid):
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        Basket.objects.create(user_id = user)
        basket = Basket.objects.filter(user_id=user, is_active=True).first()
    
    product = Product.objects.get(id=prodid)
    sbi = BasketItems.objects.filter(basket_id=basket, product_id=product).first()
    if sbi is None:
        sbi = BasketItems(basket_id=basket, product_id = product)
        sbi.save()
    else:
        sbi.quantity = sbi.quantity + 1
        sbi.save()
    return render(request, 'product_individual.html', {'product':product, 'added':True})

@login_required
def show_basket(request):
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        return render(request, 'basket.html', {'empty':True})
    else:
        sbi = BasketItems.objects.filter(basket_id=basket)
        if sbi.exists():
            return render(request, 'basket.html', {'basket':basket, 'sbi':sbi})
        else:
            return render(request, 'basket.html', {'empty':True})

@login_required
def remove_basket(request ,sbi):
    basketitem = BasketItems.objects.get(id=sbi)
    if basketitem is None:
        return redirect("/basket") 
    else:
        if basketitem.quantity > 1:
            basketitem.quantity = basketitem.quantity - 1
            basketitem.save() 
        else:
            basketitem.delete()
    return redirect("/basket")

@login_required
def order(request):
    # load in all data we need, user, basket, items
    user = request.user
    basket = Basket.objects.filter(user_id=user, is_active=True).first()
    if basket is None:
        return redirect("/")
    sbi = BasketItems.objects.filter(basket_id=basket)
    if not sbi.exists(): # if there are no items
        return redirect("/")
    # POST or GET
    if request.method == "POST":
        # check if valid
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user_id = user
            order.basket_id = basket
            total = 0.0
            for item in sbi:
                total += float(item.item_price())
            order.total_price = total
            order.save()
            basket.is_active = False
            basket.save()
            return render(request, 'ordercomplete.html', {'order':order, 'basket':basket, 'sbi':sbi})
        else:
            return render(request, 'orderform.html', {'form':form, 'basket':basket, 'sbi':sbi})
    else:
        # show the form
        form = OrderForm()
        return render(request, 'orderform.html', {'form':form, 'basket':basket, 'sbi':sbi})

@login_required
def previous_orders(request):
    user = request.user
    orders = Order.objects.filter(user_id=user)
    return render(request, 'orderhistory.html', {'orders':orders})

class UserSignupView(CreateView):
    model = APIUser
    form_class = UserSignupForm
    template_name = 'user_signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class UserLoginView(LoginView):
    template_name = 'login.html'

def logout_user(request):
    logout(request)
    return redirect("/")
