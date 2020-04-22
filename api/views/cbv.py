from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Category, Discussion, Topic, Comment
from api.serializers import CategorySerializer, DiscussionSerializer, TopicSerializer, CommentSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)


class DiscussionList(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class DiscussionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class CategoryDiscussions(APIView):
    def get(self, request, category_id):
        # category = Category.objects.get(id=category_id)
        discussions = Discussion.objects.filter(category_id=category_id)
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class TopicList(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class TopicDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class DiscussionTopics(APIView):
    def get(self, request, category_id, discussion_id):
        # category = Category.objects.get(id=category_id)
        # discussion = Discussion.objects.get(id=discussion_id)
        topics = Topic.objects.filter(discussion_id=discussion_id)
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status = status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentList(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class TopicComments(APIView):
    def get(self, request, category_id, discussion_id, topic_id):
        # category = Category.objects.get(id=category_id)
        # discussion = Discussion.objects.get(id=discussion_id)
        # topic = Topic.objects.filter(id=topic_id)
        comments = Comment.objects.filter(topic_id=topic_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
