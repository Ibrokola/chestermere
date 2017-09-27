from django.db import models

from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from about.utils import create_slug





class RegHeaderImage(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=None)

    def __str__(self):
        return str(self.title)
    
    # def get_absolute_url(self):
    #     return reverse("forms:detail")

class RegCategory(models.Model):
    title = models.CharField(max_length=500)
    # title2 = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)


class RegForm(models.Model):
    header = models.ForeignKey(RegHeaderImage, related_name='page_header')
    category = models.ForeignKey(RegCategory, related_name='section_parts')
    title = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, null=True)
    # download_file = models.FileField(null=True, blank=True)
    ext_link = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.title)

    # def get_absolute_url(self):
	# 	view_name = "products:detail_slug"
	# 	return reverse(view_name, kwargs={"slug": self.slug})


def reg_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(reg_pre_save_reciever, sender=RegForm)