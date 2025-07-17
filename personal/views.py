from django.shortcuts import render, redirect
from django.http import HttpResponse # Import HttpResponse
from .forms import ContactForm


# View function for the home screen
def home_screen_view(request):
    # Logs the request headers to the console 
    # (for debugging purposes)
    print(request.headers)
    # Renders the 'base.html' template without
    # any context data
    return render(request, "base.html", {})


def eshopping_view(request):
    # Logs the request headers to the console 
    # (for debugging purposes)
    print(request.headers)
    # Renders the 'eShopping.html' template without 
    # any context data
    return render(request, "eshopping.html", {})


def meetsetshehla_view(request):
    # Logs the request headers to the console 
    # (for debugging purposes)
    print(request.headers)
    # Renders the 'extrapage.html' template without 
    # any context data
    return render(request, "extrapage.html", {})


def order_view(request):
    if request.method == 'POST':
        # Make sure to pass request.FILES for file uploads!
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'order.html', {'form': form})

def success_view(request):
    return render(request, 'success.html', {})
    # Alternatively, for a simple text response without a template:
    # return HttpResponse("Your order has been placed successfully!")


def polls_views(request):
    # Logs the request headers to the console
    # (for debugging purposes)
    print(request.headers)
    # Renders the 'polls.html' template without
    # any context data
    return render(request, "polls.html", {})
