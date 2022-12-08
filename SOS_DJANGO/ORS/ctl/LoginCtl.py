from .BaseCtl import BaseCtl
from django.shortcuts import render,redirect
from ORS.utility.DataValidator import DataValidator
from service.service.UserService import UserService


class LoginCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]
        self.form["password"] = requestForm["password"]
    
    def input_validation(self):
        super().input_validation()
        inputError = self.form["inputError"]
        if (DataValidator.isNull(self.form["login_id"])):
            inputError["login_id"] = "Login ID can not be null"
            self.form["error"] = True
        else:
            if (DataValidator.isemail(self.form["login_id"])):
                inputError["login_id"] = "Login ID must be email"
                self.form["error"] = True

        if (DataValidator.isNull(self.form["password"])):
            inputError["password"] = "Password can not be null"
            self.form["error"] = True

        # print("FORM----------",self.form["error"])
        return self.form["error"]

    def display(self, request, params={}):
        self.form['out'] = params.get("out")
        return render(request, self.get_template(), {"form": self.form})

    def submit(self, request, params={}):
        PATH = params.get('path')
        user = self.get_service().authenticate(self.form)
        if (user is None):
            self.form["error"] = True
            self.form["message"] = "Invalid ID or Password"
            res = render(request, self.get_template(), {'form':self.form})
        else:
            print("tttttttttttt",PATH)
            request.session["user"] = user
            request.session['name'] = user.role_Name
            if PATH is None:
                res = redirect('/ORS/Welcome/')
            else:
                res = redirect(PATH)
        
        return res


    # HTML Template of Login page
    def get_template(self):
        return "Login.html"

    # Service of role
    def get_service(self):
        return UserService()