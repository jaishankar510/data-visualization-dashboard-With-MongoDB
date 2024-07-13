from django.contrib import admin


from .models import Blackcoffer
# Register your models here.
#from import_export.admin import ImportExportMinxin

from import_export.admin import ImportExportModelAdmin




    # fields =["end_year", "intensity", "sector", "topic", "insight", "url", "region", "start_year", "impact", "added", "published", "country", "relevance", "pestle", "source", "title", "likelihood"]
   


admin.site.register(Blackcoffer)
