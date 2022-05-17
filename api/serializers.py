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


class CategorySerializers():
    class List(serializers.ModelSerializer):
        name = serializers.CharField(required=True, max_length=50)
        description = serializers.CharField(allow_null=True, allow_blank=True)
        parent = serializers.PrimaryKeyRelatedField(allow_null=True, read_only=True)
        
        class Meta:
            model = models.Category
            fields = "__all__"

    class Update(List):
        parent = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=models.Category.objects.all())
        def validate(self, data):
            conds = {
                "parent_id": data["parent"].id if data["parent"] else None,
                "name": data["name"],
            }
            if models.Category.objects.filter(**conds).exists():
                raise serializers.ValidationError(
                    {"name": f"같은 레벨의 카테고리에 이미 존재하는 이름입니다."}
                )
            return data


    class Retrieve(Update):
        pass

    class Create(Retrieve):
        pass
