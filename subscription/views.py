
# this is for login and logout authentication
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
from django.shortcuts import render
# this is to send response to client
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # to resolve csrf issue
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
# model and serializer import
from .serializer import *
from .models import *
from django.core.mail import send_mail


# ******************************************************************
# Course
# *******************************************************************

class SubscriptionViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        data = Subscription.objects.all()
        serializer = SubscriptionSerializer(data, many=True)
        return Response(serializer.data)

    permission_classes = [AllowAny]

    def get_subscription(self, request, name, *args, **kwargs):
        try:
            data = Subscription.objects.filter(user_id=name)
            serializer = SubscriptionSerializer(data, many=True)
            return Response(serializer.data)
        except Subscription.DoesNotExist:
            content = 'No Data in the table'
            return Response(content, status.HTTP_401_UNAUTHORIZED)

    permission_classes = [AllowAny]

    def post_subscription(self, request, *args, **kwargs):
        json_parser = JSONParser()
        data = json_parser.parse(request)
        print('ok')
        serializer = SubscriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)
