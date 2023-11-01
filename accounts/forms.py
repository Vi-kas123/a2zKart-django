from django import forms
from .models import Account
from django.forms import ValidationError

class RegistertrationForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter password',
        'class':'form-control',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm password'
    }))
    
    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']
        
    def clean(self):
        cleaned_data = super(RegistertrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            # print("Password not match")
            raise ValidationError(
                "Password does not match!"
            )  
        
       
        
        
    def __init__(self,*args,**kwargs):  # to apply css class to fields
         super(RegistertrationForm,self).__init__(*args,**kwargs)
         self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First Name'     
         self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last Name'     
         self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter Phone Number'     
         self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'     
         
         for field in self.fields:
             self.fields[field].widget.attrs['class'] = 'form-control'    
             
             
    
        