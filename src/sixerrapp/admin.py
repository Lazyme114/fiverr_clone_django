from django.contrib import admin
from .models import Profile, Gig,Pruchase, Review

# Register your models here.
admin.site.register(Profile)
admin.site.register(Gig)
admin.site.register(Pruchase)
admin.site.register(Review)