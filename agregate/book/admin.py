from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)

class PublisherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publisher, PublisherAdmin)

class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)