from .BaseCtl import BaseCtl
from ORS.utility.DataValidator import DataValidator
from django.shortcuts import render

class LogoutCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['login_id'] = requestForm['login_id']
        self.form['password'] = requestForm['password']
    
    def input_validation(self):
        super().input_validation()
        inputError  = self.form['inputError']
        
        if (DataValidator.isNull(self.form['login_id'])):
            inputError['login_id'] = "Login Id can not be null "
            self.form['error'] = True

        if (DataValidator.isNull(self.form['password'])):
            inputError['password'] = "Password can not be null "
            self.form['error'] = True
        
        return self.form['error']

    def display(self, request, params={}):
        request.session['user'] = None
        self.form["message"] = "LOGOUT SUCCESSFULL"
        res = render(request, self.get_template(),{'form':self.form})
        return res

    
    # HTML Template of Logout page
    def get_template(self):
        return "Login.html"