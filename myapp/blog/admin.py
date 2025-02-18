from django.contrib import admin
from .models import Post,Catagory,AboutUs,Contact
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    search_fields = ("content","id","title")
    list_filter = ("catagory","created_at")


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','message')

admin.site.register(Post, PostAdmin)
admin.site.register(Catagory)
admin.site.register(AboutUs)
admin.site.register(Contact,ContactAdmin)