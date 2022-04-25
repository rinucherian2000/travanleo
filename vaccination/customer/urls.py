from django.urls import path
from customer import  views

urlpatterns=[
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("signin",views.SignInView.as_view(),name="signin"),
    path("home",views.CustomerHome.as_view(),name="home"),
    path("home/addtoslot/<int:id>",views.AddSlot.as_view(),name="addtoslot"),
    path("home/addtoslot/list",views.CartView.as_view(),name="listtocart"),
    path("home/remove/<int:id>",views.Removeslot.as_view(),name="removed"),




]