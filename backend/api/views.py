from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models

# Create your views here.

class createLostItem(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request):
        
        if (request.data is None or 
            request.data.heading is None or request.data.description is None):
            # bad request recieved from user
            return Response(data=None, status=400)

        
        createdItem = LostItem.objects.create(heading = request.data.heading, description = request.data.description)


        if (createdItem is not None):
            return Response(status=200)

        else:
            return Response(status=500)


class deleteLostItem(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request):
        
        if (request.data is None or 
            request.data.id):
            # bad request recieved from user
            return Response(data=None, status=400)

        

        LostItem.delete(request.data.id)

        



        

        




