from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from django.contrib.auth.models import User

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    # def get(self, request):
    #     items = Booking.objects.all()
    #     serializer = BookingSerializer(items, many=True)
    #     return Response(serializer.data)  # return JSON


# inheriting the rest_framework.generics.ListCreateView class. 
# It handles the POST and GET method calls
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer 
    permission_classes = [IsAuthenticated]   

# inherits the RetrieveUpdateAPIView and DestroyAPIView classes both 
# imported from the rest_framework.generics module. 
# This class is responsible for processing GET, PUT and DELETE method calls.
class SingleMenuItemView(generics.RetrieveAPIView, generics.DestroyAPIView, 
    generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated] 


# class MenuView(APIView):
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuSerializer(items, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)  # return JSON

#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status.HTTP_201_CREATED)        