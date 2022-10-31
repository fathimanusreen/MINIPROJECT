from django.contrib import admin

from user.models import Profile

# Register your models here.
admin.site.site_header="Movie Ticket Booking"


admin.site.register(Profile)