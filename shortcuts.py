from django.shortcuts import render_to_response
from django.template import RequestContext

# a shorter form of render_to_response
rtr = lambda x,y,z: render_to_response(x, y, context_instance=RequestContext(z))

