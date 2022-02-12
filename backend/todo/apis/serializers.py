from todo_app import models
from rest_framework import serializers

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title','description')
        model = models.Todo 