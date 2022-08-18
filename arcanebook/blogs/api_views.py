from logging import raiseExceptions
from queue import Empty
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework import authentication, permissions



class LoginView(APIView):

    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong !'

        try:
            # first we make sure user data should not be Empty
            data = request.data
            if data.get('username') is None:
                response['message'] = "Username must not be empty"
                raiseExceptions("Username must not be empty")
            elif data.get('password') is None:
                response['message'] = "Password must not be empty"
                raiseExceptions("Password must not be empty")
            
            user_exist = User.objects.filter(username = data.get('username')).first()

            if user_exist is None:
                response['message'] = 'User not exist !'
                raiseExceptions('User not exist !')
            else:
                user_obj = authenticate(username=data.get('username'),password = data.get('password'))
                if user_obj:
                    try:
                        print(user_obj)
                        login(request,user_obj)
                    except Exception as e:
                        print(e)
                    response['message'] = "Welcome to Arcanebook"
                    response['status'] = '200'
                else:
                    response['message'] = "invalid credintials"

        except Exception as post_req_exception:
            print(post_req_exception)

        return Response(response)

class RegisterView(APIView):

    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong !'

        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = "Username must not be empty"
                raiseExceptions("Username must not be empty")
            elif data.get('password') is None:
                response['message'] = "Password must not be empty"
                raiseExceptions("Password must not be empty")

            user_exist = User.objects.filter(username = data.get('username')).first()

            if user_exist is not None:
                response['message'] = 'User already exist'
            else:
                user_obj = User.objects.create(**request.data,is_staff=False,is_superuser=True)
                print(user_obj)

                user_obj.set_password(request.data.get('password'))
                user_obj.save()
                response['message'] = 'Account Created Succesfully !'

        except Exception as e:
            print(e)
        return Response(response)


class LogoutView(APIView):
    def post(self,request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong !'
        
        try:
            logout(request)
            response['status'] = '200'
            response['message'] = "You logged out succesfully."
        except Exception as e:
            print(e)
            response['message'] = "Technical issue"
        return Response(response)

        








LoginView = LoginView.as_view()
RegisterView = RegisterView.as_view()
LogoutView = LogoutView.as_view()