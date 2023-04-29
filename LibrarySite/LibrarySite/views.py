from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from staff.models import Home, AboutCorousel, AboutText, AboutLibrarian, BooksNewArrival, BooksTopPicks, ContactDetails, Notice
# from staff.models import Home, AboutCorousel, AboutText, AboutLibrarian, BooksNewArrival, BooksTopPicks


def home(request):
    
    homecontent = Home.objects.all()
    aboutCorousel = AboutCorousel.objects.all()
    aboutText = get_object_or_404(AboutText,Sno=1)
    aboutPatron = AboutLibrarian.objects.get(Sno = 1)
    aboutlibrarian = AboutLibrarian.objects.get(Sno = 2)
    booksNewArrival = BooksNewArrival.objects.all()
    booksTopPicks = BooksTopPicks.objects.all()
    contactDetails = ContactDetails.objects.get(Sno = 1)
    notice = Notice.objects.all()

    aboutText = aboutText.text
    aboutText=aboutText.split("\n")
    

    aboutPatronText=aboutPatron.text
    aboutPatronText=aboutPatronText.split("\n") 

    aboutlibrarianText=aboutlibrarian.text
    aboutlibrarianText=aboutlibrarianText.split("\n")

    abt = list()
    for i in aboutCorousel:
        abt.append([i.image,i.position])
    abt.sort(key=lambda x: x[1])

    bna = list()
    for i in booksNewArrival:
        bna.append([i.image,i.position])
    bna.sort(key=lambda x: x[1])

    btp = list()
    for i in booksTopPicks:
        btp.append([i.image,i.position])
    btp.sort(key=lambda x: x[1])
    
    print(list(aboutCorousel))
    context = {'homecontent' : homecontent,
               'aboutCorousel':abt,
               'aboutText': aboutText, 
               'aboutPatron':aboutPatron, 
               'aboutPatronText':aboutPatronText, 
               'aboutlibrarian':aboutlibrarian, 
               'aboutlibrarianText':aboutlibrarianText, 
               'booksNewArrival': bna,
               'booksTopPicks':btp,
               'contactDetails':contactDetails,
               'notices':notice}
    
    return render(request, "home.html", context)

def staffSignin(request):
    if request.method == "POST":

        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username = loginusername, password = loginpassword)
        if user is None:
            messages.error(request, "Invalid Credentials, Please check and retry again")
            return redirect('home') 
        else:
            login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect('staff')
    else:
        HttpResponse("404 - Not Found")


def staffLogout(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('home')