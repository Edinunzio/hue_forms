from django import forms

class SigninForm(forms.Form):
    bridge_ip = forms.IPAddressField()
    username = forms.CharField()