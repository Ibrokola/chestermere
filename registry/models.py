from django.db import models






class RegHeaderImage(models.Model):
    image = models.ImageField(upload_to='images/')
    intro = models.CharField(max_length=200)

    def __str__(self):
        return str(self.image)


class Section(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return str(self.title)



class RegForm(models.Model):
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=300)
    download_file = models.FileField(null=True, blank=True)
    ext_link = models.CharField(max_length=1000, null=True, blank=True)


    def __str__(self):
        return str(self.title)