from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
from .forms import UserAdminCreationForm,LoginForm
from django.contrib.auth import authenticate, login


class UserCreration(TemplateView):
    def get(self, request, *args, **kwargs):
        form=UserAdminCreationForm()
        conetxt={}
        conetxt["form"]=form
        return render(request,"registration.html",conetxt)

    def post(self, request, *args, **kwargs):
        form=UserAdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("inside")
        conetxt = {}
        conetxt["form"] = form
        return render(request, "registration.html", conetxt)
class LoginView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {}
        context["form"] = form
        return render(request, "login.html", context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                print("authenticated")
                return redirect("register")
