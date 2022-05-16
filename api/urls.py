from django.urls import path

from . import utils, views

# path("모델/", 모델목록조회및생성클래스.as_view(), name="모델")
get_path_with_model_name = lambda name: path(
    f"{utils.camel_to_snake(name)}/",
    views.class_dict[f"{name}ListCreateAPIView"].as_view(),
    name=name
)

# path("모델/<str:pk>/", 모델조회및수정및삭제클래스.as_view(), name="모델")
get_path_with_model_name_and_pk = lambda name: path(
    f"{utils.camel_to_snake(name)}/<str:pk>/",
    views.class_dict[f"{name}RetrieveUpdateDestroyAPIView"].as_view(),
    name=name
)

urlpatterns = [
    path('', views.getHome, name="홈페이지"),
    *[get_path_with_model_name(name) for name in utils.model_names],
    *[get_path_with_model_name_and_pk(name) for name in utils.model_names],
]
