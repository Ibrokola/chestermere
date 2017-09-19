from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.translation import ugettext_lazy as _

from django.utils.text import slugify
from about.utils import create_slug


class CertHeader(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=None)

    def __str__(self):
        return str(self.title)



class CertCategory(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=None)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.title)
    
    # def get_absolute_url(self):
    #     return reverse("cert:detail",kwargs={"slug": self.slug})

def cert_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(cert_pre_save_reciever, sender=CertCategory)