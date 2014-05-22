from django.db import models
from mezzanine.core.fields import RichTextField
from mezzanine.pages.models import Page


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"{}".format(self.name)


class ProjectPage(Page):
    cover_image = models.ImageField(upload_to="page_images", blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to="page_images", blank=True, null=True)
    category = models.ForeignKey(Category)
    project_description = RichTextField()


class ProjectImage(models.Model):
    image = models.ImageField(upload_to="project_images")
    project_page = models.ForeignKey(ProjectPage)