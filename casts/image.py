from django.db import models
# from django.utils.html import mark_safe
import os


class Photo(models.Model):
    image = models.ImageField('Image', upload_to='uploads/images/fossil', null=True, blank=True)
    fossil = models.ForeignKey('Fossil', on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(null=True, blank=True)
    default_image = models.BooleanField(default=False)

    def thumbnail(self):
        if self.image:  # test that the photo has an image.
            image_url = os.path.join(self.image.url)
            return mark_safe('<a href="{}"><img src="{}" style="width:300px" /></a>'.format(image_url, image_url))
        else:
            return None

    thumbnail.short_description = 'Image'
    thumbnail.allow_tags = True
    thumbnail.mark_safe = True
