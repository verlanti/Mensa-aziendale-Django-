from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy



class RegisterForm(UserCreationForm):

    email = forms.EmailField(label = "Email")
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required = True)

    class Meta:
        model = User
        fields = ("username","password1","password2","email","group")
       

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.password1 = self.cleaned_data["password1"]
        user.password2 = self.cleaned_data["password2"]
        user.email = self.cleaned_data["email"]
        user.group = self.cleaned_data["group"]

        if commit:
            user.save()
        return user
