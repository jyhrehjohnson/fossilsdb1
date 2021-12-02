from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Fossil
from .models import Photo
from .models import Primate

'''This program modifies the Django admin interface to produce a
new database/app cataloging the hominin and primate fossil casts
housed in the University of Texas at Austin's Anthropology Department.'''


class PhotosInline(admin.StackedInline):  # Add the Photo class to admin
    model = Photo  # define the model being displayed
    extra = 0  # set the "extra" characters to 0 as it is just an image
    readonly_fields = ('thumbnail',)  # in the read only headers have the title 'thumbnail'
    fieldsets = [  # create the field sets for user in put
        ('Photos', {
            'fields': [('default_image', 'image', 'thumbnail', 'description')]})]


'''ImportExportModelAdmin allows the user to import data from a given file. It also
allows the fossil/primate information to be exported to csv, html, json, etc. files
as an output.'''


class FossilAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [  # create the field sets for user in put
        ('Fossil Information',
         {'fields': ['catalog_number', 'ut_catalog_id', 'scientific_name', 'is_type_specimen',
                     'ut_storage_location', 'site', 'age', 'description', 'remarks']})
    ]
    readonly_fields = ('default_image',)
    list_display = [  # create the list display
        'catalog_number', 'ut_catalog_id', 'scientific_name', 'is_type_specimen', 'ut_storage_location', 'site', 'age',
        'default_image']
    list_filter = ['catalog_number', 'ut_catalog_id', 'scientific_name']  # set what can be filtered
    search_fields = ['catalog_number', 'scientific_name']  # set what can be searched
    inlines = [
        # ReferenceInline, # the number of references significantly slows page loads
        PhotosInline,
    ]


class PrimateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    fieldsets = [  # create the field sets for user in put
        ('Cast Information',
         {'fields': ['catalog_number', 'ut_catalog_id', 'scientific_name', 'ut_storage_location', 'site',
                     'description', 'remarks', 'default_image']})
    ]
    readonly_fields = ('default_image',)
    list_display = (  # create the list display
        'catalog_number', 'ut_catalog_id', 'scientific_name', 'ut_storage_location', 'site',
        'default_image')
    list_filter = ['catalog_number', 'ut_catalog_id', 'scientific_name']  # set what can be filtered
    search_fields = ['catalog_number', 'scientific_name']  # set what can be searched


admin.site.register(Fossil, FossilAdmin)  # register the classes to the admin site
admin.site.register(Primate, PrimateAdmin)  # register the classes to the admin site
