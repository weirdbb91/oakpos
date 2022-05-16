from rest_framework import serializers

from . import models

# 각각의 메소드에 해당하는 범위로 생성

class MemberSerializers():
    class List(serializers.ModelSerializer):
        name = serializers.CharField(max_length=255)
        
        class Meta:
            model = models.Member
            exclude = ["is_guest", "created_at", "updated_at"]
    
    class Update(List):
        is_guest = serializers.BooleanField()
        
        class Meta:
            model = models.Member
            exclude = ["created_at", "updated_at"]
    
    class Retrieve(Update):
        pass
    
    class Create(Retrieve):
        pass
