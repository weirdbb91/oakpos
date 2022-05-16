from django.http import JsonResponse
from rest_framework import generics

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
