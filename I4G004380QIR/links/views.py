from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView , UpdateAPIView, DestroyAPIView
from .serializers import LinkSerializer
from .models import Link



# Create your views here.
class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(active = True)
    serializer_class = LinkSerializer
