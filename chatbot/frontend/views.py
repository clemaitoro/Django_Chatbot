from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def frontend(request, slug=None):
    # return HttpResponse("""
    #     <p> Hello from the frontend </p>
    # """)
    return render(request, 'frontend/template_chatbot.html')