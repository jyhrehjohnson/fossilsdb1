from django.db import models  # import models from the django database
import os
from django.utils.safestring import mark_safe

'''This program modifies the Django admin interface to produce a 
new database/app cataloguing the hominin and primate fossil casts 
housed in the University of Texas at Austin's Anthropology Department.'''

'''Create classes for Fossil and Primate casts. For models with 
character fields a max length must be set. Image fields need an 
area to be uploaded to. For all input, except catalog_number, set 
null=True and blank=True. This lets the user save the cast information
without these fields needing to be filled in at the time of submission.
'''


class Fossil(models.Model):  # create class for fossil casts
    """
    Model for fossil object
    """
    catalog_number = models.CharField(max_length=200)
    # collection_code = models.CharField("UT")
    # item_part = models.CharField("a,b,c,d")
    # ut_catalog_id = models.CharField(collection_code, id, item_part)
    ut_catalog_id = models.CharField(max_length=200, null=True, blank=True)
    scientific_name = models.CharField(max_length=200, null=True, blank=True)
    site = models.CharField(max_length=200, null=True, blank=True)
    is_type_specimen = models.BooleanField('Type Specimen', default=False)
    ut_storage_location = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)

    def default_image(self):
        """
        Function to fetch a default thumbnail image for a fossil
        :return:
        """
        images = self.photo_set.filter(default_image=True)
        if images.count() >= 1:
            return images[0].thumbnail()
        else:
            return None

    default_image.short_description = 'Fossil Thumbnail'  # Set the title of the image in the list
    default_image.allow_tags = True
    default_image.mark_safe = True


class Primate(models.Model):  # create class for primate casts

    catalog_number = models.CharField(max_length=200)
    ut_catalog_id = models.CharField(max_length=200, null=True, blank=True)
    scientific_name = models.CharField(max_length=200, null=True, blank=True)
    site = models.CharField(max_length=200, null=True, blank=True)

    ut_storage_location = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.CharField(max_length=200, null=True, blank=True)

    def default_image(self):
        """
        Function to fetch a default thumbnail image for a primate
        :return:
        """
        images = self.photo_set.filter(default_image=True)
        if images.count() >= 1:
            return images[0].thumbnail()
        else:
            return None

    default_image.short_description = 'Fossil Thumbnail'
    default_image.allow_tags = True
    default_image.mark_safe = True


'''Create a Photo class to upload a photo of the fossil/primate'''


class Photo(models.Model):
    image = models.ImageField('Image', upload_to='fossils', null=True, blank=True)  # tell the database where to upload
    fossil = models.ForeignKey('Fossil', on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=True)  # add a field for a description of the image
    default_image = models.BooleanField(default=False)  # create a checkbox for if you would like it to be the default

    '''test that the photo has an image.'''

    def thumbnail(self):
        if self.image:
            image_url = os.path.join(self.image.url)
            return mark_safe('<a href="{}"><img src="{}" style="width:300px" /></a>'.format(image_url, image_url))
        else:
            return None

    thumbnail.short_description = 'Image'
    thumbnail.allow_tags = True
    thumbnail.mark_safe = True

    class Meta:
        managed = True
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
