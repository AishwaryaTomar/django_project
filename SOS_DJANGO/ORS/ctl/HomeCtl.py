from django.shortcuts import render
from .BaseCtl import BaseCtl

class HomeCtl(BaseCtl):

    # HTML Template of Home page
    def get_template(self):
        return "Home.html"

    def display(self, request, params={}):
        print("--------------->",request)
        return render(request, self.get_template())

    def submit(self, request, params={}):
        pass

    def get_service(self):
        pass

    