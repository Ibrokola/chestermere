from django.db import models

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from about.utils import create_slug


class ImageHeader(models.Model):
    image = models.ImageField(upload_to='images/')
    # service = models.ForeignKey('Service', on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    intro = models.TextField(max_length=None)


    def __str__(self):
        return str(self.title)


class Service(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=None, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
    #     return reverse("services:detail",kwargs={"slug": self.slug})

def service_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(service_pre_save_reciever, sender=Service)