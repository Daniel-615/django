from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project
        fields=('id','title','description','technology','created_at')
        read_only_fields=('created_at',) #con esto no permite actualizarlo

