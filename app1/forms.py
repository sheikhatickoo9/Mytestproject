from django import forms
from app1.models import Register
class RegisterForm(forms.ModelForm):
    class Meta():
        model =Register
        exclude=[" userId",
                 "firstName",
                 "lastName",
                 " Email",
                 "Image",
                 "userMobile",
                 "isActive"]
