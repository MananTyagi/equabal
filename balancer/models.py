from django.db import models

# Create your models here.
class reactions(models.Model):
    sno=models.AutoField(primary_key=True)
    reactant1=models.CharField( max_length=10,blank=False)
    rcoe1=models.IntegerField(blank=False)
    reactant2=models.CharField( max_length=10,blank=False)
    rcoe2=models.IntegerField(blank=False)
    product1=models.CharField( max_length=10,blank=False)
    pcoe1=models.IntegerField(blank=False)
    product21=models.CharField( max_length=10,blank=False)
    pcoe2=models.IntegerField(blank=False,default=None)
    def __str__(self):
        return self.reactant1+" "+self.reactant2
    
