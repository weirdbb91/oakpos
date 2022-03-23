from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def getHome(request):
    return JsonResponse("홈페이지", json_dumps_params={"ensure_ascii": False}, safe=False)
