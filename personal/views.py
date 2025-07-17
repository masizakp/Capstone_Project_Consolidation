from django.shortcuts import render, redirect
from django.http import HttpResponse  # Import HttpResponse
from .forms import ContactForm


def home_screen_view(request):
    """
    Handles the home screen view.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered 'base.html' template without context
    :rtype: HttpResponse
    """
    print(request.headers)
    return render(request, "base.html", {})


def eshopping_view(request):
    """
    Handles the eShopping page view.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered 'eshopping.html' template without context
    :rtype: HttpResponse
    """
    print(request.headers)
    return render(request, "eshopping.html", {})


def meetsetshehla_view(request):
    """
    Handles the extrapage view.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered 'extrapage.html' template without context
    :rtype: HttpResponse
    """
    print(request.headers)
    return render(request, "extrapage.html", {})


def order_view(request):
    """
    Handles order form submission and rendering.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Redirect to 'success' page if POST and form valid; else renders 'order.html' with form
    :rtype: HttpResponse
    """
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'order.html', {'form': form})


def success_view(request):
    """
    Displays success page after order submission.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered 'success.html' template without context
    :rtype: HttpResponse
    """
    return render(request, 'success.html', {})


def polls_views(request):
    """
    Handles the polls page view.

    :param request: HTTP request object
    :type request: HttpRequest
    :return: Rendered 'polls.html' template without context
    :rtype: HttpResponse
    """
    print(request.headers)
    return render(request, "polls.html", {})
