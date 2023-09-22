from rest_framework import serializers
from .models import Person



class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id','code', 'picture', 'rank', 'plec', 'added_at')

class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('picture', 'plec')
    
class PersonUpdateRatingSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=8,default='ur_old')
    enymycode = serializers.CharField(max_length=8,default='ur_old2')
    rank = serializers.IntegerField(default=800)
    enymyrank = serializers.IntegerField(default=800)
   

        
