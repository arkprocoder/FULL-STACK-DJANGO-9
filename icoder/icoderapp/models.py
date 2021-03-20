from django.db import models

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authname=models.CharField(max_length=15)
    img=models.ImageField(upload_to='pics',blank=True,null=True)
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=12)
    desc=models.TextField()
    
    def __str__(self):
        return self.name
    
