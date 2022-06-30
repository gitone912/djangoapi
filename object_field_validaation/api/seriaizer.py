
from rest_framework import serializers
from .models import student

def start_with_k(value):
    if value[0].lower == 'k':
        raise serializers.ValidationError('k named peoples are banned')
    
class studentserializer(serializers.Serializer):
    name =serializers.CharField(max_length=50 ,validators=[start_with_k])
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
    
    #fieldlvl validation
    def validate_roll(self,value):
        if value>= 200:
            raise serializers.ValidationError('seat full')
        return value

    def validate(self,data):
        nm= data.get('name')
        ct= data.get('city')
        if nm.lower()=='klee' and ct.lower()=='monstad':
            raise serializers.ValidationError('klee is banned from this city')
        return data
#validator