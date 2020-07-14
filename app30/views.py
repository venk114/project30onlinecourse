from django.shortcuts import render
from django.views.generic import TemplateView,View,CreateView,ListView
from django.http import HttpResponse
from app30.models import ScheduleNewClass


class AdminLogin(TemplateView):
    template_name = "adminlogin.html"

class LoginCheck(View):
    def post(self,request):
        un = request.POST.get("t1")
        up = request.POST.get("t2")
        if un == "naveen" and up == "Na1":
            return render(request,"menu.html")
        else:
            return render(request,"adminlogin.html",{"error":"Invalid User"})


class NewClass(CreateView):
    template_name = "new_class.html"
    model = ScheduleNewClass
    fields = "__all__"

class AllCourse(ListView):
    template_name = "view_all.html"
    model = ScheduleNewClass
class Home(TemplateView):
    template_name = "home.html"