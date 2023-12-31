
from rest_framework import serializers
from .models import Student, userRank, Ip

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class userRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = userRank
        fields = "__all__"
        
class IpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ip
        fields = "__all__"