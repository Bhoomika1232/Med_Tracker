from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Medicine(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE, related_name='medicines')
    name=models.CharField(max_length=200)
    dosage=models.CharField(max_length=200, help_text='e.g. 500 mg or 2ml')
    frequency=models.CharField(max_length=100, help_text='2 times/day')
    notes=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.dosage}-{self.frequency})"
    