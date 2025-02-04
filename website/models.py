from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        
    def __str__(self):
        return self.message
    
class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self) -> str:
        return self.email