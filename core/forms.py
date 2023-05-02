from django import forms 
from .models import Customer
from django.forms import ModelForm
from django.forms import ModelForm, Textarea

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            "text": Textarea(attrs={"cols": 60, "rows": 10,'placeholder':'请输入您想咨询的信息：如出国打工咨询、韩国劳务咨询、出国留学等','class':'form-control'}),
            # "name": forms.TimeInput(attrs={'placeholder':'请留下您的姓名','class':'form-control'}),
            # "phone": forms.TimeInput(attrs={'placeholder':'请留下您的电话','class':'form-control'}),
            # "phone":
        }

    name = forms.CharField(widget=forms.TimeInput(attrs={'placeholder':'请留下您的姓名','class':'form-control'}))
    phone = forms.CharField(widget=forms.TimeInput(attrs={'placeholder':'请留下您的电话','class':'form-control'}))
    


