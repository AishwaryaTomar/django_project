from .BaseCtl import BaseCtl
from ORS.utility.DataValidator import DataValidator
from django.shortcuts import render
from service.models import User
from service.service.EmailMessage import EmailMessage
from service.service.EmailService import EmailService
from service.service.ForgetPasswordService import ForgetPasswordService

class ForgetPasswordCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['login_id'] = requestForm['login_id']
    
    # Validate Form
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]

        if (DataValidator.isNull(self.form['login_id'])):
            inputError['login_id'] = "Login ID can not be null"
            self.form["error"] = True
        else:
            if (DataValidator.isemail(self.form['login_id'])):
                inputError['login_id'] = "Login ID must be like student@gmail.com"
                self.form["error"] = True

        return self.form["error"]

    def display(self, request,params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        q = User.objects.filter(login_id = self.form['login_id'])
        userList = ""
        for userData in q:
            userList = userData
        if userList != "":
            emsg = EmailMessage()
            emsg.to = [userList.login_id]
            emsg.subject = "Forget Password"
            mailResponse = EmailService.send(emsg,"forgotPassword",userList)
            if mailResponse == 1:
                self.form['error'] = False
                self.form['message'] = "PLEASE CHECK YOUR MAIL, YOUR PASSWORD HAS BEEN SENT SUCCESSFULLY"
                request.session['user'] = userList
                res = render(request, self.get_template(), {'form': self.form})
            else:
                self.form['error'] = True
                self.form['message'] = "Please check your Internet Connection"
                res = render(request, self.get_template(), {'form': self.form})
        else:
            self.form["error"] = True
            self.form["message"] = "Login Id is Incorrect"
            res = render(request, self.get_template(), {'form': self.form})
        return res
    
    # HTML Template of ForgetPassword page
    def get_template(self):
        return "ForgetPassword.html"

    def get_service(self):
        return ForgetPasswordService()