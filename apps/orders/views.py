from django.shortcuts import render, redirect

def list_orders(request):
    return render(request,'ordenes/list_orders.html')

def create_task(request):
    print(request.POST)
    return redirect('/orders/')