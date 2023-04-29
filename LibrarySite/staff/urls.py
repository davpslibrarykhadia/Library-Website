from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('', views.staff, name="staff"),
    path('/edit_home', views.edit_home, name="edit_home"),
    path('/editAboutCourosel', views.edit_aboutCorousel, name="editAboutCourosel"),
    path('/deleteAboutCorousel', views.delete_about_corousel, name="deleteAboutCorousel"),
    path('/editAboutText', views.edit_aboutText, name="editAboutText"),
    path('/addNewImageCourosel', views.about_addNewImageCorousel, name="addNewImageCourosel"),
    path('/editOurPatron', views.editOurPatron, name="editOurPatron"),
    path('/editTheLibrarian', views.editTheLibrarian, name="editTheLibrarian"),

    path('/editNewArrivalBooks', views.editNewArrivalBooks, name="editNewArrivalBooks"),
    path('/deleteNewArrivalBooks', views.deleteNewArrivalBooks, name="deleteNewArrivalBooks"),
    path('/addImageNewArrivalBooks', views.addImageNewArrivalBooks, name="addImageNewArrivalBooks"),

    path('/editTopPicksBooks', views.editTopPicksBooks, name="editTopPickBooks"),
    path('/deleteTopPicksBooks', views.deleteTopPicksBooks, name="deleteTopPicksBooks"),
    path('/addImageTopPicksBooks', views.addImageTopPicksBooks, name="addImageTopPicksBooks"),

    path('/deleteContactMessage', views.deleteContactMessage, name="deleteContactMessage"),
    path('/editContactDetails', views.editContactDetails, name="editContactDetails"),
    path('/notice', views.editNoticeDetails, name="editNoticeDetails"),


    
]