from django.contrib import admin
from .models import Book, Comment
from django.contrib.auth.models import Group

admin.site.site_header = 'BookenT.com'
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name','manager','author','category','date', 'status')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
admin.site.unregister(Group)