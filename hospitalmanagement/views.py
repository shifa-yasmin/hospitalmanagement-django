from django.shortcuts import render
from .models import Doctor,Patient
# Create your views here.

def home(request):
    return render(request,"home.html")
def doctors(request):
    doctors=Doctor.objects.all()
    return render(request,"doctors.html",{"doctors":doctors})
def patients(request):
    patients=Patient.objects.all()
    return render(request,patients.html,{"patients":patients})