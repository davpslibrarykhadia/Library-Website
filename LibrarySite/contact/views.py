from django.shortcuts import render, redirect, HttpResponse
from contact.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == "POST":
        print("hello")
        name = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        


        if len(name) < 3 or len(email)<5 or  len(subject)<3 or  len(message) < 1:
            messages.error(request,"Please fill the form properly")
        
        else:
            contact = Contact(name = name, email = email, subject = subject, message = message)
            contact.save()
            messages.success(request, "Your response has been submitted succesfully")
        return redirect('/')
    else:
        return HttpResponse("404 - Page Not Found")

