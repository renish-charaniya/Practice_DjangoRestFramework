from rest_framework import serializers
from .models import Student



class StudentModelSerializer(serializers.ModelSerializer):
    # Validators
    def starts_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should start with R')

    name=serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']
        # read_only_fields=['name','roll']
        # extra_kwargs={'name':{'read_only':True},'city':{'read_only':True}}

    # Field level validation
    def validate_roll(self, value):
        if value >= 50:
            raise serializers.ValidationError("No Vacancy")
        return value

    # Object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'AAArjun' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data


'''
#Validators
def starts_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should start with R')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[starts_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # Field level validation
    def validate_roll(self,value):
        if value >= 50:
            raise serializers.ValidationError("No Vacancy")
        return value

    #Object level validation
    def validate(self, data):
        nm=data.get('name')
        ct=data.get('city')
        if nm.lower()=='rohit' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data

'''