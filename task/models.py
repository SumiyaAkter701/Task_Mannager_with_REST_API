from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Task(models.Model):
    PRIORITY = (('Low', 'Low'),('Medium', 'Medium'),('High', 'High'),)

    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)


    title = models.CharField(max_length=300)
    description = models.TextField()
    due_date =models.DateTimeField()
    priority = models.CharField(choices=PRIORITY, default='Medium', max_length=20)
    is_complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False,blank=True,null=True)
    completed_date = models.DateTimeField(auto_now_add=True,editable=False,blank=True,null=True)
    updated_date = models.DateField(auto_now=True, editable=False)
    
    
    def __str__(self) -> str:
        return self.title
    

class Task_Image(models.Model):
    task = models.ForeignKey(Task,on_delete=models.CASCADE,related_name='image',blank=True,null=True)

    image= models.ImageField(upload_to='Task-Image')

    def __str__(self) -> str:
        return self.image.name