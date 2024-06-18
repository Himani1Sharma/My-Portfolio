from django import forms
# from .models import MyModel

class MyModelForm(forms.Form):
    name = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
    # class Meta:
    #     model = MyModel
    #     fields = ['name', 'email', 'phone', 'company', 'message']
