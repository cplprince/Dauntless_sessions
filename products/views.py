from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .forms import ProductModelForm
from .models import Product

def home_view(request, *args, **kwargs):
    context = {"name": "abc"}
    return render(request, "home.html", context)

def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = ProductModelForm()
    return render(request, "forms.html", {"form": form})


def product_detail_view(request, pk):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 
    return render(request, "products/detail.html", {"object": obj})


def product_api_detail_view(request, pk, *args, **kwargs):
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not found"})
    return JsonResponse({"id": obj.id})
    