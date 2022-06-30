from rest_framework import serializers
from .models import student


class studentserializer(serializers.ModelSerializer):
    class Meta:
        model= student
        fields=['id','name','roll','city']
        #validation mehods from here
        #read_only_fields=['name','city']
        
    