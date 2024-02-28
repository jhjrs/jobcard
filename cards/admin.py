from django.contrib import admin

# Register your models here.
from .models import JobCard
from .models import Photo

admin.site.register(JobCard) 

admin.site.register(Photo)