from django.db import models


# Create your models here.
class voter_Details(models.Model):
    voter_id = models.CharField(primary_key=True, max_length=20)
    name = models.CharField(max_length=255)
    dob = models.DateField()
    mobile = models.CharField(max_length=15)
    is_voted = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'voter'
        verbose_name_plural = 'voters'

    # def __str__(self):
    #     return '{}'.format(self.name)

class oppositions(models.Model):
    op_id = models.CharField(primary_key=True,max_length=20)
    party_name= models.CharField(max_length=255)
    candidate_name= models.CharField(max_length=255)
    vote_count= models.IntegerField(default=0)

    def _str_(self):
        return self.c_party

class voteends(models.Model):
    checkk=True
    def __str__(self):
        return self.checkk


