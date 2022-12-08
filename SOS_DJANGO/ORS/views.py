from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.models  import Session
from django.http import HttpResponse

from .ctl.HomeCtl import HomeCtl
from .ctl.LoginCtl import LoginCtl
from .ctl.BaseCtl import BaseCtl
from .ctl.RegistrationCtl import RegistrationCtl
from .ctl.WelcomeCtl import WelcomeCtl
from .ctl.UserCtl import UserCtl
from .ctl.CollegeCtl import CollegeCtl
from .ctl.CourseCtl import CourseCtl
from .ctl.MarksheetCtl import MarksheetCtl
from .ctl.RoleCtl import RoleCtl
from .ctl.StudentCtl import StudentCtl
from .ctl.SubjectCtl import SubjectCtl
from .ctl.AddFacultyCtl import AddFacultyCtl
from .ctl.TimeTableCtl import TimeTableCtl
from .ctl.ChangePasswordCtl import ChangePasswordCtl
from .ctl.LogoutCtl import LogoutCtl
from .ctl.MyProfileCtl import MyProfileCtl
from .ctl.UserListCtl import UserListCtl
from .ctl.CollegeListCtl import CollegeListCtl
from .ctl.CourseListCtl import CourseListCtl
from .ctl.MarksheetListCtl import MarksheetListCtl
from .ctl.MarksheetMeritListCtl import MarksheetMeritListCtl
from .ctl.RoleListCtl import RoleListCtl
from .ctl.StudentListCtl import StudentListCtl
from .ctl.SubjectListCtl import SubjectListCtl
from .ctl.AddFacultyListCtl import AddFacultyListCtl
from .ctl.TimeTableListCtl import TimeTableListCtl
from .ctl.ForgetPasswordCtl import ForgetPasswordCtl

# Create your views here.

def index(request):
    return render(request,'project.html')

@csrf_exempt
def action(request, page, action=""):
    ctlName = page + "Ctl()"
    ctlObj = eval(ctlName)
    return ctlObj.execute(request, {"id":0})


@csrf_exempt
def actionID(request, page="", operation="", id=0):
    print("RRRRRRRR",request)
    path = request.META.get('PATH_INFO')
    print("AAAAAAAAAAAAAAA",path)

    if request.session.get('user') is not None and page != "":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        res = ctlObj.execute(request, {"id":id})
    elif page == "Registration":
        ctlName = "Registration" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id":id})
    elif page == "Home":
        ctlName = "Home" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id":id})
        print("HOME__________",page)
    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "Ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id":id})
    elif page == "Login":
        ctlName = page + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = None
        # print("MMMMMMMMMMMMMM", request.session.get('msg'))
        res = ctlObj.execute(request, {"id":id})

    else:
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        request.session['msg'] = "Your session has been expired, please login again."
        res = ctlObj.execute(request, {"id":id, "path":path})
        print("PPPPPPP",id,path)
    return res

@csrf_exempt
def auth(request, page="", operation="", id=0):
    if page == "Logout":
        Session.objects.all().delete()
        request.session['user'] = None
        out = "LOGOUT SUCCESSFULL"
        ctlName = "Login" + "Ctl()"
        ctlObj = eval(ctlName)
        
        res = ctlObj.execute(request, {"id":id, "operation":operation, "out":out})

    elif page == "ForgetPassword":
        ctlName = "ForgetPassword" + "ctl()"
        ctlObj = eval(ctlName)
        res = ctlObj.execute(request, {"id":id, "operation":operation})

    return res


# To remove favicon error

def GET(self):
    return HttpResponse("Hello Guys")



