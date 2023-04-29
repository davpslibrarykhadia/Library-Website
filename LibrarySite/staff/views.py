from django.shortcuts import render, redirect, HttpResponse, get_object_or_404,HttpResponsePermanentRedirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Home,AboutCorousel,AboutText,AboutLibrarian,BooksNewArrival,BooksTopPicks,ContactDetails, Notice
from contact.models import Contact
# Create your views here.
from pathlib import Path
import os
def delete_file(file_dir):
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = os.path.join(BASE_DIR,file_dir)
    os.remove(path)


def staff(request):
    
    homecontent = Home.objects.all()
    aboutCorousel = AboutCorousel.objects.all()
    aboutPatron = AboutLibrarian.objects.get(Sno = 1)
    aboutlibrarian = AboutLibrarian.objects.get(Sno = 2)
    booksNewArrival = BooksNewArrival.objects.all()
    booksTopPicks = BooksTopPicks.objects.all()
    contacts = Contact.objects.all()
    contactDetails = ContactDetails.objects.get(Sno = 1)
    aboutText = AboutText.objects.get(Sno = 1)
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

    
  
    context = {'homecontent' : homecontent, 'contacts': contacts,'aboutText': aboutText,'aboutPatronText': aboutPatronText, 'aboutlibrarianText': aboutlibrarianText,
               'aboutCorousel':abt, 'aboutPatron':aboutPatron, 'aboutlibrarian':aboutlibrarian, 'booksNewArrival': bna, 'booksTopPicks': btp,
               'contactDetails':contactDetails}
    
   
    return render(request, "staff.html", context)

def edit_home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        line3 = request.POST['line3']
        home = get_object_or_404(Home,Sno=1)
        if uploaded_file is not None:
            fs = FileSystemStorage(location='static/uploads/home')
            fs.save(uploaded_file.name, uploaded_file)
            old_image = home.image
            home.image = uploaded_file.name
            home.save()
          
            delete_file(f'static\\uploads\\home\\{old_image}')  
           
        if line1:
            home.line_1= line1
            home.save()
        if line2:
            home.line_2 = line2
            home.save()
        if line3:   
            home.line_3 = line3
            home.save()
        if line1 == False and line2==False and line3==False and uploaded_file is None:
            messages.error(request, "Invalid details Provided Please check and try again")
            return redirect('staff')    
        
        messages.success(request, "Home Section Editted Successfully")
        return redirect('staff')
        
    else:
        return render(request, 'staff.html')
        

def edit_aboutCorousel(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('image')
        lpos=request.POST['lpos']
        lastimage=request.POST['lastimage']
        npos=request.POST['npos']

        about = get_object_or_404(AboutCorousel,position=lpos,image = lastimage)
        if uploaded_file is not None:
            fs = FileSystemStorage(location='static/uploads/about')
            fs.save(uploaded_file.name, uploaded_file)
            old_image = about.image
            about.image=uploaded_file.name
            about.save()
            delete_file(f'static\\uploads\\about\\{old_image}') 

        if npos:
            about.position=npos
            about.save()

        if uploaded_file is None and npos is False:
            messages.error(request, "You didnot choose anything, Please check and try again")
            return redirect('staff')
        
        
        
        messages.success(request, "Selected data is seccessfully modified")
  
        return redirect('staff')
        
    else:
        return render(request, 'staff.html')


def delete_about_corousel(request):
    if request.method == 'POST':
        
        corousel_id = request.POST.get('corousel_id')
        lastimage=request.POST['lastimage']
 
        corousel = AboutCorousel.objects.get(position=corousel_id,image = lastimage).delete()
        delete_file(f'static\\uploads\\about\\{lastimage}')
        messages.success(request, "Selected Corousel Deleted Successfully")
        return redirect('staff')    

    
    else:
        return render(request, 'staff.html')
    
def edit_aboutText(request):
    if request.method == 'POST':
        ntext = request.POST.get('ntext')
        aboutText = get_object_or_404(AboutText,Sno=1)
        aboutText.text = ntext
        aboutText.save()
        messages.success(request, "About Section Text Updated Succesfully")
        return redirect('staff')    
    
    else:
        return render(request, 'staff.html')



def about_addNewImageCorousel(request):
    if request.method == 'POST':

        npos = request.POST['npos']
        uploaded_file = request.FILES.get('image')
        
        fs = FileSystemStorage(location='static/uploads/about')
        fs.save(uploaded_file.name, uploaded_file)
        corousel = AboutCorousel(image = uploaded_file.name,position = npos)
        corousel.save()

        messages.success(request, "New Image added Successfully to the Corousel")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    
def editOurPatron(request):

    if request.method == 'POST':

        title = request.POST['title']
        ntext = request.POST['ntext']
        uploaded_file = request.FILES.get('image')
        patron = AboutLibrarian.objects.get(Sno = 1)

        if uploaded_file is not None:
            
            fs = FileSystemStorage(location='static/uploads/librarian')
            fs.save(uploaded_file.name, uploaded_file)
            lastimage = patron.image
            patron.image = uploaded_file.name
            patron.save()

            delete_file(f'static\\uploads\\librarian\\{lastimage}')

        if ntext:
            patron.text=ntext
            patron.save()

        if title:
            patron.title=title
            patron.save()

        if uploaded_file is None and ntext is False and title is False:
            messages.error(request, "You do not choose anything.  Please check and try again")
            return redirect('staff')
        
        messages.success(request, "Your changes made Successfully.")
        return redirect('staff')
    
    else:
        return render(request, 'staff.html')


def editTheLibrarian(request):

    if request.method == 'POST':
        title = request.POST['title']
        ntext = request.POST['ntext']
        uploaded_file = request.FILES.get('image')
        patron = AboutLibrarian.objects.get(Sno = 2)


        if uploaded_file is not None:
            
            fs = FileSystemStorage(location='static/uploads/librarian')
            fs.save(uploaded_file.name, uploaded_file)
            lastimage = patron.image
            patron.image = uploaded_file.name
            patron.save()

            delete_file(f'static\\uploads\\librarian\\{lastimage}')

        if ntext:
            patron.text=ntext
            patron.save()

        if title:
            patron.title=title
            patron.save()

        if uploaded_file is None and ntext is False and title is False:
            messages.error(request, "You do not choose anything. Please check and try again")
            return redirect('staff')
        
        messages.success(request, "Your changes made Successfully.")
        return redirect('staff')
    
    else:
        return render(request, 'staff.html')
    

def editNewArrivalBooks(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('image')
        lpos=request.POST['lpos']
        lastimage=request.POST['lastimage']
        npos=request.POST['npos']
        about = get_object_or_404(BooksNewArrival,position=lpos,image = lastimage)
        if uploaded_file is not None:
            # try:
            about.image=uploaded_file.name
            about.save()
            delete_file(f'static\\uploads\\books\\new_arrival\\{lastimage}')
         
            fs = FileSystemStorage(location='static/uploads/books/new_arrival')
            fs.save(uploaded_file.name, uploaded_file)
            messages.success(request, "Selected Book Modified Successfully")
        
        if npos:
            about.position = npos
            about.save()
        if uploaded_file is None and npos is False:
            messages.error(request, "You didn't choose anything, Please check and try again later")

        messages.success(request, "Your changes updated successfully")
        return redirect('staff')
    else:
        return render(request, 'staff.html')
    
def deleteNewArrivalBooks(request):
    if request.method == 'POST':

        image = request.POST['lastimage']
        book_pos = request.POST['book_pos']

        query = get_object_or_404(BooksNewArrival, position = book_pos, image = image).delete()
        delete_file(f'static\\uploads\\books\\new_arrival\\{image}')
        messages.success(request, "Selected Image deleted Successfully from New Arrival")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    
def addImageNewArrivalBooks(request):
    if request.method == 'POST':

        npos = request.POST['npos']
        uploaded_file = request.FILES.get('image')
        
        corousel = BooksNewArrival(image = uploaded_file.name,position = npos)
        corousel.save()

        fs = FileSystemStorage(location='static/uploads/books/new_arrival')
        fs.save(uploaded_file.name, uploaded_file)
        messages.success(request, "New Image added Successfully to the New Arrival")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    

def editTopPicksBooks(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('image')
        lpos=request.POST['lpos']
        lastimage=request.POST['lastimage']
        npos=request.POST['npos']
        about = get_object_or_404(BooksTopPicks,position=lpos,image = lastimage)

        if uploaded_file is not None:
            # try:
            about.image=uploaded_file.name
            about.save()
            
            delete_file(f'static\\uploads\\books\\top_picks\\{lastimage}')
            
            fs = FileSystemStorage(location='static/uploads/books/top_picks')
            fs.save(uploaded_file.name, uploaded_file)

        if npos:
            about.position = npos
            about.save()
        if uploaded_file is None and npos is False:
            messages.error(request, "You didn't choose anything, Please check and try again later")
            
        messages.success(request, "Your changes updated successfully")
        return redirect('staff')
    else:
        return render(request, 'staff.html')
 

     
def deleteTopPicksBooks(request):
    if request.method == 'POST':

        image = request.POST['lastimage']
        book_pos = request.POST['book_pos']

        query = get_object_or_404(BooksTopPicks, position = book_pos, image = image).delete()
        delete_file(f'static\\uploads\\books\\top_picks\\{image}')
        messages.success(request, "Selected Image deleted Successfully from Top Picks")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
 


    
def addImageTopPicksBooks(request):
    if request.method == 'POST':

        npos = request.POST['npos']
        uploaded_file = request.FILES.get('image')
        
        corousel = BooksTopPicks(image = uploaded_file.name,position = npos)
        corousel.save()

        fs = FileSystemStorage(location='static/uploads/books/top_picks')
        fs.save(uploaded_file.name, uploaded_file)
        messages.success(request, "New Image added Successfully to the Corousel")
        return redirect('staff')

    else:
        return render(request, 'staff.html')
    

def deleteContactMessage(request):
    if request.method == 'POST':
        sno = request.POST['sno']
        query = get_object_or_404(Contact, Sno = sno).delete()
        messages.success(request, "Selected Message deleted Successfully from Contact Message")
        return redirect('staff')

    else:
        return render('staff.html')
    
def editContactDetails(request):
    if request.method == 'POST':
        
        query = get_object_or_404(ContactDetails, Sno = 1)
        name = request.POST['name']
        address = request.POST['address']
        email = request.POST['email']

        if name:
            query.name = name
            query.save()
        if address:
            query.address = address
            query.save()
        if email:
            query.email = email
            query.save()
        if name is False and address is False and email is False:
            messages.error(request, "You did not provide any details, Please check and try again")
            return redirect('staff')
        
        messages.success(request, "Selected Message deleted Successfully from Contact Message")
        return redirect('staff')

    else:
        return render('staff.html')
 

def editNoticeDetails(request):
    if request.method == 'POST':
        notices=get_object_or_404(Notice, Sno=1)
        message = request.POST['notice']
        notices.notice = message
        notices.save()
        messages.success(request, 'Notice Updated Successfully ')

        return redirect('staff')
    
    else:
        messages.error(request, 'Something Went wrong, Please check and try again')
        return redirect('staff')


