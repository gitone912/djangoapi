from rest_framework import serializers
from .models import student

class studentserializer(serializers.Serializer):
    name =serializers.CharField(max_length=50)
    roll =serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    ability = serializers.CharField(max_length=55)
    
    def create(self,validate_data):
        return student.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        print(instance.name)
        instance.name = validate_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validate_data.get('roll',instance.roll)
        instance.city = validate_data.get('city',instance.city)
        instance.ability = validate_data.get('ability',instance.ability)
        instance.save()
        return instance