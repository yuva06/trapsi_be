from django.db import models
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail
from drf_extra_fields.fields import Base64ImageField
from django.utils import timezone

class Blog(models.Model):
    
    choice =(
        ('tech','TECH'),
        ('angular','ANGULAR'),
        ('reactjs','REACTJS'),
        ('ui/ux','UI/UX'),
    )

    description = models.TextField()
    is_enabled = models.BooleanField(default=True)
    image = models.ImageField( blank = False , null= False)
    name = models.CharField(max_length=120)
    category = models.CharField(max_length=120 , choices=choice , default='examupdate')
    mini_description = models.CharField(max_length=120)



    @property
    def image_tag(self):
        if self.image:
            _thumbnail = get_thumbnail(self.image, '200x200', upscale= False, crop = False, quality=100)
            return format_html('<img src="{}" width="{}" height="{}"/>'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    def __str__(self):
        return self.description

class RegistrationApplication(models.Model):
    
    name= models.CharField(max_length=120)
    mobileno= models.CharField(max_length=120)
    email= models.CharField(max_length=180)
    date= models.DateField(auto_now_add=True)
    course= models.CharField(max_length=120)
    
 
    def __str__(self):
        return self.name

class ClientForm(models.Model):
    
    name= models.CharField(max_length=120)
    mobileno= models.CharField(max_length=180)
    email= models.CharField(max_length=180)
    company= models.CharField(max_length=180)
    date= models.DateField(auto_now_add=True)
    
    intrest= models.TextField()
    subject= models.TextField()
 
    def __str__(self):
        return self.name


class Enquire(models.Model):

    choice =(
        ('not talk','NOT TALK'),
        ('pending','PENDING'),
        ('confirmed','CONFIRMED'),
    )
    
    name_or_company = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)
    mobileno= models.CharField(max_length=120)
    service = models.CharField(max_length=220)
    qutation_cost= models.CharField(max_length=120)
    process = models.CharField(max_length=120 , choices=choice , default='not talk')

 
    def __str__(self):
        return self.name_or_company


class Client(models.Model):

    name_or_company = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)
    mobileno= models.CharField(max_length=120)
    service = models.CharField(max_length=220)
    start_date = models.DateField()
    End_date = models.DateField()
    account_details = models.TextField()
    payment = models.TextField()

    def __str__(self):
        return self.name_or_company