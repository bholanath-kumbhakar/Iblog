
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=90)
    description=models.CharField(max_length=4000,blank=True,null=True)
    published_at=models.DateTimeField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    # slug=models.SlugField(max_length=250,null=True,blank=True)

    def __str__(self) -> str:
        return self.title


#contct us model

class Contact_Us(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    mobile=models.IntegerField()
    message=models.TextField(max_length=250)
#like model

class Like(models.Model):
    created_at=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    like=models.BooleanField(default=False)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
