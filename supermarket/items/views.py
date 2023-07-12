from django.shortcuts import render,redirect
from django .views .generic import View,CreateView
from .forms import RegForm,LogForm
from django.contrib.auth import authenticate,login,logout
from django .urls import reverse_lazy
# Create your views here.

class LogView(View):
    def get(self,request):
        form=LogForm()
        return render(request,"log.html",{"f":form})
    def post(self,request):
        fdata=LogForm(data=request.POST)
        if fdata.is_valid():
            uname=fdata.cleaned_data.get("username")
            pswd=fdata.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                return redirect("products")
            else:
                return render(request,"log.html",{"f":fdata})
    
class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{"data":form})
    def post(self,request):
        fdata=RegForm(data=request.POST)
        if fdata.is_valid():
            fdata.save()
            return redirect("log")
        else:
            return render(request,"reg.html",{"form":fdata})



def index(request):
    return render(request, 'navigation.html')


class lgOut(View):
    def get(self,request):
        logout(request)
        return redirect("log")