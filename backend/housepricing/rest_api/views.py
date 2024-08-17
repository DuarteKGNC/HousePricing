from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .LRegression.main import start


@api_view(['GET'])
def predict(request):
    start()
    return Response(status=200)