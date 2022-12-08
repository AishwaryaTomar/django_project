from django.http import HttpResponse
from abc import ABC, abstractmethod

'''
Base class is inherited by all application controllers
'''

class BaseCtl(ABC):
    # Contains preload data
    preload_data = {}  #class variable

    # Contains list of objects, it will be displayed at list page
    page_list = {}     #class variable

    '''
    Initialize controller attributes
    '''

    def __init__(self):
        self.form = {}
        self.form["id"] = 0
        self.form["message"] = ""
        self.form["error"] = False
        self.form["inputError"] = {}
        self.form["pageNo"] = 1

    '''
    It loads preload data of the page
    '''
    
    def preload(self,request):
        print("This is Preload")

    '''
    execute method is executed for each HTTP request.
    It calls display() or submit() method for
    HTTP Get and HTTP Post methods respectively.   
    '''

    def execute(self, request, params={}):
        self.preload(request)
        if "GET" == request.method:
            print("This is execute------",params)
            return self.display(request, params)
        elif "POST" == request.method:
            self.request_to_form(request.POST)
            if self.input_validation():
                return self.display(request, params)
            else:
                if (request.POST.get("operation") == "Delete"):
                    return self.deleteRecord(request, params)
                elif (request.POST.get("operation") == "next"):
                    return self.next(request, params)
                elif (request.POST.get("operaion") == "previous"):
                    return self.previous(request, params)
                else:
                    return self.submit(request, params)
        else:
            message = "Request is not supported"
            return HttpResponse(message) 


    '''
    Apply input validation
    '''
    
    def input_validation(self):
        self.form["error"] = False
        self.form["message"] = ""
        
    '''
    METHODS
    '''   
    # delete record of received ID
    def deleteRecord(self, request, params={}):
        pass
    
    # populate values from Request GET/POST to Controller form object
    def request_to_form(self, requestForm):
        pass
    
    # populate Form from Model
    def model_to_form(self, obj):
        pass

    # convert/send form to model
    def form_to_model(self, obj):
        pass
                
    ''' ABSTRACT METHODS '''

    # submit data
    @abstractmethod
    def submit(self, request, params={}):
        pass

    # display data
    @abstractmethod
    def display(self, request, params={}):
        pass

    # returns template of controller

    @abstractmethod
    def get_template(self):
        pass

    @abstractmethod
    def get_service(self):
        pass

    