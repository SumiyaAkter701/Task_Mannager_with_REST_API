from .models import Task
from rest_framework import serializers

class Task_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields =['id','title','description','due_date','priority','is_complete']
