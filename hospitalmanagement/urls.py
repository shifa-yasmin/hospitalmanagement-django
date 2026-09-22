
from django.urls import path,include
from .views import home,patients,doctors

urlpatterns = [
    path("",home,name="home"),
    path("doctors/",doctors,name="doctors"),
    path("patients/",patients,name="patients")
]