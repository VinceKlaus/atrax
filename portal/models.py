from django.contrib.auth.models import Permission, User
from django.db import models


class LiteratureType(models.Model):
    lit_type_name = models.CharField(max_length=250)

    def __str__(self):
        return self.lit_type_name


class Literature(models.Model):
    user = models.ForeignKey(User, default=1)
    lit_type = models.ForeignKey(LiteratureType, on_delete=models.CASCADE)
    lit_author = models.CharField(max_length=250)
    lit_title = models.CharField(max_length=250)
    lit_desc = models.TextField(max_length=1000, null=True)
    lit_file = models.FileField(default='')

    def __str__(self):
        return self.lit_title + ' by ' + self.lit_author
