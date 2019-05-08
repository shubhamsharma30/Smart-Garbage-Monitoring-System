from django import forms
from login.models import UserProfileInfo, D_Details
from django.contrib.auth.models import User
from .models import C_Details, Trashcan1

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = UserProfileInfo
		fields = ('name','contact_no')


class D_Form(forms.ModelForm):
	class Meta:
		model = D_Details
		fields = ('Name','Address','Ph_no','Truck_no')

class C_Form(forms.ModelForm):
	#C_Password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = C_Details
		fields = ('C_Name', 'C_Address', 'C_Ph_no','C_D_id','C_Dustbin_ID')


class T_Form(forms.ModelForm):
	class Meta:
		model = Trashcan1
		fields = ('T_ID', 'T_x_c', 'T_y_c','T_C_id','T_D_id')
