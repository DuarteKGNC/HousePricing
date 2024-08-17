from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .LRegression.use_models import make_predict


@api_view(['POST'])
def predict(request):
    data = request.data['data']
    result = make_predict(data)
    return Response(data={'data':result},status=200)