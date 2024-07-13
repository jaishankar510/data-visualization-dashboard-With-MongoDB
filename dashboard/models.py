from django.db import models
#from .models import *
# Create your models here.
from djongo import models

from django.contrib import admin


 #_id = models.ObjectIdField()
#_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

from import_export.admin import ImportExportModelAdmin


class Blackcoffer(models.Model):
    end_year = models.CharField(max_length=50,blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True, default=00000)
    sector =  models.CharField(max_length=100,blank=True, null=True)
    topic = models.CharField(max_length=100,blank=True, null=True)
    insight = models.CharField(max_length=200,blank=True, null=True, default=00000)
    url =  models.URLField(max_length=200,blank=True, null=True)
    region = models.CharField(max_length=100,blank=True, null=True)
    start_year = models.CharField(max_length=50, blank=True, null=True)
    impact = models.CharField(max_length=100,blank=True, null= True)
    added = models.CharField(max_length=100,blank=True, null=True)
    published = models.CharField(max_length=100,blank=True, null=True)
    country = models.CharField(max_length=100,blank=True, null=True)
    relevance = models.IntegerField(blank=True, null=True, default=00000)
    pestle = models.CharField(max_length=100,blank=True, null=True)
    source = models.CharField(max_length=50,blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    likelihood = models.IntegerField(blank=True, null=True, default=00000)
    
    def __str__(self):
        return f'{self.topic}---{self.title}'
    
    
    
class TaskAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    class Meta:
        model = Blackcoffer()    
    
    
