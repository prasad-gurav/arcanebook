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
                    login(request,user_obj)
                    response['message'] = "Welcome to Arcanebook"
                    response['status'] = '200'
                else:
                    response['message'] = "invalid credintials"

        except Exception as post_req_exception:
            print(post_req_exception)

        return Response(response)


LoginView = LoginView.as_view()