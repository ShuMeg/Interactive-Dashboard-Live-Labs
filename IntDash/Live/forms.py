# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import newResource
  
# create a ModelForm
class newResourceForms(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = newResource
        fields = "__all__"