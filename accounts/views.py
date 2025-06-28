from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from django.http import HttpResponse
class RegisterView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        return Response({'msg': 'User created successfully'})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': f'Welcome {request.user.username}'})



from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_form(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return HttpResponse("Login Successful")
        return HttpResponse("Invalid credentials")
    return render(request, 'login.html')


def home(request):
    return render(request,'home.html')
