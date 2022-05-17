from collections import defaultdict

from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from . import models, serializers, utils

# Create your views here.

def getHome(request):
    return JsonResponse("홈페이지", json_dumps_params={"ensure_ascii": False}, safe=False)


queryset_dict = {
    # https://docs.djangoproject.com/en/4.0/ref/models/querysets/#prefetch-related
    # JOIN이 필요한 쿼리셋의 경우 이곳에 아래와 같은 방식으로 추가
    
    # from django.db.models import Prefetch
    
    # "Restaurant": models.Restaurant.objects.prefetch_related(
    #     Prefetch(
    #         "pizzas",
    #         to_attr="menu"
    #     ),
    #     Prefetch(
    #         "pizzas",
    #         queryset = models.Pizza.objects.filter(vegetarian=True),
    #         to_attr="vegetarian_menu"
    #     ),
    #     "vegetarian_menu__toppings"
    # )
}

class CommonListCreateAPIView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.serializer_class.List
        if self.request.method == "POST":
            return self.serializer_class.Create

class CommonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_serializer_class(self):
        if self.request.method == "GET":
            return self.serializer_class.Retrieve
        if self.request.method in ["PUT", "PATCH"]:
            return self.serializer_class.Update
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class_dict = {}

for name in utils.model_names:
    class_dict[f"{name}ListCreateAPIView"] = type(
        f"{name}ListCreateAPIView",
        (CommonListCreateAPIView,),
        {
            "queryset": queryset_dict[name] if name in queryset_dict.keys() \
                else getattr(models, name).objects.all(),
            "serializer_class": getattr(serializers, f"{name}Serializers"),
        }
    )
    class_dict[f"{name}RetrieveUpdateDestroyAPIView"] = type(
        f"{name}RetrieveUpdateDestroyAPIView",
        (CommonRetrieveUpdateDestroyAPIView,),
        {
            "queryset": queryset_dict[name] if name in queryset_dict.keys() \
                else getattr(models, name).objects.all(),
            "serializer_class": getattr(serializers, f"{name}Serializers"),
        }
    )


# [카테고리] 반환시 하위 카테고리 목록이 담길 상위 카테고리의 필드 이름
sub_name = serializers.CategorySerializers.List.SUB_NAME

def set_sub_list(top_category_list, subcategory_dict):
    for category in top_category_list:
        category[sub_name] = subcategory_dict[category["id"]]
        if category[sub_name]:
            set_sub_list(category[sub_name], subcategory_dict)

# [카테고리] 카테고리는 계층구조를 만들어 반환한다
def category_list(self, request, *args, **kwargs):
        subcategory_dict = defaultdict(list)
        
        serializer = self.get_serializer(self.get_queryset(), many=True)
        for category in serializer.data:
            subcategory_dict[category["parent"]].append(category)
        
        set_sub_list(subcategory_dict[None], subcategory_dict)
        return Response(subcategory_dict[None])

# [카테고리] CategoryListCreateAPIView의 GET 메소드를 오버라이딩한다
class_dict[f"CategoryListCreateAPIView"].get = category_list
