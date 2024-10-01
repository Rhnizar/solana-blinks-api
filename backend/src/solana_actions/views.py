from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def Test(request):
    return JsonResponse({"message": "Here will implement Solana actions and blinks."})