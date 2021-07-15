from django.shortcuts import redirect, render
from .models import Product,Order

# Create your views here.
product_data =[
  
]
def product_page(request):
    product_data= Product.objects.all()
    if request.method =="POST":
        product_id = request.POST['product_id']
        print(product_id)
        name = Product.objects.get(pk=product_id)
        neworder = Order(product = name)
        neworder.save()
        return redirect('all_placed_orders')
    return render(request,'products/products.html',{'all_products':product_data})
    

def orders_placed_page(request):
    order_all = []
    order_all = Order.objects.all()
    return render(request,'products/orders.html',{'allorders':order_all})


    