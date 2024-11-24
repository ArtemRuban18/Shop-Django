from django.db import models
import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False, unique=True)
    slug = models.SlugField(blank=False)

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name