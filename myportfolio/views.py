#from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render, redirect
# from .forms import MyModelForm

# def submit_form(request):
#     if request.method == 'POST':
#         form = MyModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = MyModelForm()
#     return render(request, 'index-image.html', {'form': form})

# def success(request):
#     return render(request, 'success.html')

from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

#Create your views here

def index(request):
    if request.method == "POST":
        contact = MyModel()
        name = request.POST.get('name')
        company = request.POST.get('company')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # contact.name = name
        # contact.company = company
        # contact.email = email
        # contact.phone = phone
        # contact.message = message
        contact.save()
        return HttpResponse("<h1> Thanks for contact us </h1>")

    return render(request, 'index-image.html')
