
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
# importing "random" for random operations
import random
from django.db import Error

from userprofile.views import *
# ****************************************************
# USER REGISTRATION PROCESS
# ****************************************************


@csrf_exempt
def UserViewSet(request, format=None):

    if request.method == "POST":
        json_parser = JSONParser()
        data = json_parser.parse(request)

        print('ok')
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            # generate otp
            serializer.save()
            phone_number = serializer.data.get('phone_number')
            name = serializer.data.get('name')
            ## name = serializer.data.get('name')
            otp = GenerateOtp(phone_number)
            # send mail to the email address
            # create Entry of the user in the profile table WE have to create a function to insert the data
            insert_user(phone_number, name)
            # redirect to the varification page -- done at fron end
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)


# **********************************************************
# post views for the login and send some user information
# *********************************************************


class LoginViewSet(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # TO get data from the request object
        user = request.data.get('username')
        # validate that user exists in the database
        phone_number = User.objects.filter(phone_number=user)
        # if user does not exists in the database send massage need to register
        if (phone_number.count() == 0):
            content = 'User Does not exists please register'
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        # If user exists in the data base check for the varification
        else:
            phone_active = Varification.objects.filter(phone_number_id=user)
            # if data for the user daoes not exists in the varification table
            if (phone_active.count() == 0):
                # generate otp and send and ask for varification redirect it to varification page
                otp = GenerateOtp(user)
                content = 'Phone number is not validated please validate'
                return Response(content, status=status.HTTP_403_FORBIDDEN)

            # if data for the user exists in the varification table then cheack the varification status
            else:
                # validate the validation and counter accordingly respons
                data = Varification.objects.get(phone_number_id=user)
                # check the varification status on the varification table if not varified
                if (data.phone_varification != 'done'):
                    # generate otp and send and ask for varification redirect it to varification page
                    otp = GenerateOtp(user)
                    content = 'Phone number is not validated please validate'
                    return Response(content, status=status.HTTP_403_FORBIDDEN)
                # If varification is allready in the varification table
                else:
                    serializer = self.serializer_class(
                        data=request.data, context={'request': request})
                    serializer.is_valid(raise_exception=True)
                    user = serializer.validated_data['user']
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({
                        'token': token.key,
                        'phone_number': user.phone_number,
                        'name': user.name
                    })

# **********************************************************
# post view for the email varification
# *********************************************************


class VarificationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def post_auth(self, request, *args, **kwargs):
        # post method to validate the key

        phone_number = request.data.get('phone_number')
        otp = request.data.get('phone_otp')
        otp = int(otp)
        # get otp from the table
        try:
            data = PhoneOtp.objects.get(phone_number_id=phone_number)
            # compare the otp
            if (otp == data.phone_otp):
                # cretae a entry in the varification table
                Varification.objects.filter(phone_number_id=phone_number).create(
                    phone_number_id=phone_number,
                    phone_varification='done'
                )
                # varification successfulle please login
                return Response('varification successfulle please login')
            else:
                content = 'Validation Unsuccesfull - Please check your OTP'
                return Response(content, status.HTTP_401_UNAUTHORIZED)

        except PhoneOtp.DoesNotExist:
            content = 'No Data in the table'
            return Response(content, status.HTTP_401_UNAUTHORIZED)


# ******************************************************************
# sent mail function
# *******************************************************************


def SendEmail(email_address):
    subject = "Email Varification"
    message = "Please find the key here"
    from_email = "alok_kumar@nanduniversity.com"
    to_email = email_address

    send_mail(subject, message, from_email, [to_email], fail_silently=False,)

# ******************************************************************
# generate OTP function
# *******************************************************************


def GenerateOtp(phone_number):
    # return (random.randrange(100000, 999999))
    # check otp exists in the otp table or not
    try:
        data = PhoneOtp.objects.get(phone_number_id=phone_number)
        otp = (random.randrange(100000, 999999))
        PhoneOtp.objects.filter(phone_number_id=phone_number).update(
            phone_otp=otp,
            counter=data.counter+1
        )
        return otp
    except PhoneOtp.DoesNotExist:
        # otp generated
        otp = (random.randrange(100000, 999999))
        # save otp to the otp table
        PhoneOtp.objects.create(
            phone_number_id=phone_number,
            phone_otp=otp,
            counter=1
        )
        return otp
