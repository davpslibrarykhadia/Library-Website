from django.contrib import admin
from .models import Home,AboutCorousel,AboutText,AboutLibrarian,BooksNewArrival,BooksTopPicks,ContactDetails, Notice
# Register your models here.

admin.site.register(Home)
admin.site.register(AboutCorousel)
admin.site.register(AboutText)
admin.site.register(AboutLibrarian)
admin.site.register(BooksTopPicks)
admin.site.register(BooksNewArrival)
admin.site.register(ContactDetails)
admin.site.register(Notice)
