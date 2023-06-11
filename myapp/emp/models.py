from django.db import models

# Create your models here.
class Emp(models.Model):
   name=models.CharField(max_length=200)
   emp_id=models.CharField(max_length=200)
   phone=models.PositiveIntegerField() 
   address=models.CharField(max_length=150)
   working=models.BooleanField(default=True)
   department=models.CharField(max_length=10)

   # to show name in admin panel
   def __str__(self):
     return self.name
   

class Testimonial(models.Model):
   name=models.CharField(max_length=200)
   testimonial=models.TextField()
   photo=models.ImageField(upload_to="testimonials/")
   rating=models.IntegerField(max_length=1)

   def __str__(self):
      return self.testimonial