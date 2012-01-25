from solidstate.shortcuts import rtr

def home(request):
    return rtr('blog/home.html', {}, request) 
