from django.db import models
from users.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator

class Kitob(models.Model):
    name=models.CharField(max_length=255)
    kitob_beti=models.IntegerField()
    aftor=models.CharField(max_length=100)
    image=models.ImageField(upload_to='kitob_image',null=True,blank=True)
    kitob_tili=models.ForeignKey('Tillar',on_delete=models.CASCADE,related_name='tillar')
    matn=models.TextField(max_length=99999999999999,null=True,blank=True)

    def __str__(self):
        return self.name

class Tillar(models.Model):
    name=models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE,related_name='izohlar')
    comment_text=models.CharField(max_length=255,null=True,blank=True)
    stars_given=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_at=models.DateField(default=timezone.now)
