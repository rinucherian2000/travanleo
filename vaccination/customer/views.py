from django.shortcuts import render,redirect
from customer.forms import UserRegisterationForm
from django.views.generic import View,ListView
from customer.forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from owner.models import Vaccin
from customer.models import AddToSolt
from django.db.models import Sum

# Create your views here.


class SignUpView(View):
    def get(self,request):
        form=UserRegisterationForm()
        context={"form":form}
        return render(request,"signup.html",context)
    def post(self,request):
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "signup.html")
        else:
            context = {"form": form}
            return render(request, "signin.html", context)


class SignInView(View):
    def get(self,request):
        form=LoginForm()
        context={"form":form}
        return render(request,"signin.html",context)
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user= authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                if request.user.is_superuser:
                    return redirect("addvaccin")
                else:
                    return redirect("home")
            else:
                context = {"form": form}
                return render(request, "signin.html", context)


class CustomerHome(View):
    def get(self,request,*args,**kwargs):
        vaccin=Vaccin.objects.all()
        context = {"vaccinated":vaccin}
        return render(request, "cust_index.html", context)


class AddSlot(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        slot=Vaccin.objects.get(id=id)
        user=request.user
        cart=AddToSolt(item=slot,user=user)
        cart.save()
        print("Add To slot")
        return redirect("home")

class CartView(ListView):
    model = AddToSolt
    template_name ="slot_item.html"
    context_object_name = "vaccin"

    # def get(self,request,*args,**kwargs):
    #     logged_user=self.model.objects.filter(user=self.request.user,status="nonvaccinated")
    #     context={"vaccinate":logged_user,}
    #     return render(request,self.template_name,context)

class Removeslot(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        cart=AddToSolt.objects.get(id=id)
        cart.status="cancel"
        cart.save()
        return redirect("listtocart")