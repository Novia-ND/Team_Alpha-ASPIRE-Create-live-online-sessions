from django import forms

class studentForm(forms.Form):
    name = forms.CharField(max_length=254)
    email = forms.CharField(max_length=254)
    password = forms.CharField(max_length=254)

class teacherForm(forms.Form):
    name = forms.CharField(max_length=254)
    age = forms.CharField()
    education  = forms.CharField(max_length=254)
    job = forms.CharField(max_length=254)
    email = forms.CharField(max_length=254)
    password = forms.CharField(max_length=254)

class courseForm(forms.Form):
    name = forms.CharField(max_length=254)
    course = forms.CharField(max_length=254)
    info  = forms.CharField(max_length=254)
    date = forms.CharField(max_length=254)
    link = forms.CharField(max_length=254)

class LoginForm(forms.Form):
    Email = forms.CharField(max_length=254)
    Password = forms.CharField(max_length=254)



