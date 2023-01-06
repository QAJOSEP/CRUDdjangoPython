from rest_framework.viewsets import ModelViewSet
from post.models import Post
from post.api.serializers import PostSerilizer

class PostApiViewSet(ModelViewSet):
    serializer_class = PostSerilizer
    queryset = Post.objects.all()