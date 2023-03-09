from rest_framework import viewsets

from .models import BlogPost
from .serializers import BlogPostSerializer
from . import permissions


class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsOwnerOrReadOnly]
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
