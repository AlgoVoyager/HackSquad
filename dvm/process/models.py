from django.db import models


# Create your models here.
class voter(models.Model):
    voter_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    unique_code = models.CharField(max_length=8, unique=True)
    is_voted = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'voter'
        verbose_name_plural = 'voters'

    def __str__(self):
        return '{}.format(self.name)'
