from django.contrib import admin
from .models import AboutPage
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(AboutPage)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)