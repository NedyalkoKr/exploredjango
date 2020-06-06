import tagulous
from django.contrib import admin
from .models import Person, Hobbies


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'skills', 'hobbies')
    list_filter = ('name', 'title', 'skills', 'hobbies')

tagulous.admin.register(Person, PersonAdmin)


class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('name',)

tagulous.admin.register(Hobbies, HobbiesAdmin)