from django.shortcuts import render, HttpResponseRedirect
from .forms import  ProductRegistration
from .models import Product
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.

# Class for showing the Items
class ProductAddShowView(TemplateView):
  template_name = 'autopus_app/addandshow.html'
  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    fm = ProductRegistration()
    prod = Product.objects.all()
    context = {'stu':prod, 'form':fm}
    return context
  
  def post(self, request):
    fm = ProductRegistration(request.POST)
    if fm.is_valid():
      title = fm.cleaned_data['tittle']
      warnty = fm.cleaned_data['warnty']
      price = fm.cleaned_data['price']
      desc = fm.cleaned_data['desc']
      reg = Product(tittle=title, price=price, warnty=warnty, desc=desc)
      reg.save()
    return HttpResponseRedirect('/')

# This Class will Update/Edit
class ProductUpdateView(View):
  def get(self, request, id):
    pi = Product.objects.get(pk=id)
    fm = ProductRegistration(instance=pi)
    return render(request, 'autopus_app/updatestudent.html', {'form':fm})
  
  def post(self, request, id):
    pi = Product.objects.get(pk=id)
    fm = ProductRegistration(request.POST, instance=pi)
    if fm.is_valid():
      fm.save()
    return render(request, 'autopus_app/updatestudent.html', {'form':fm})

# This Class will Delete
class ProductDeleteView(RedirectView):
  url = '/'
  def get_redirect_url(self, *args, **kwargs):
    del_id = kwargs['id']
    Product.objects.get(pk=del_id).delete()
    return super().get_redirect_url(*args, **kwargs)











