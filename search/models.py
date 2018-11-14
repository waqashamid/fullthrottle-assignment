from django.db import models

# Create your models here.

class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Word(Base):

    body = models.CharField(max_length=256, db_index=True   )
    frequency = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.body