from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from wiki.models import Page
from api.serializers import PageSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

class PageList(ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageDetails(RetrieveDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
