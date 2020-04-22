from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Category, Discussion
from api.serializers import CategorySerializer, DiscussionSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)


class DiscussionList(generics.ListCreateAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = (IsAuthenticated,)


class DiscussionDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    # permission_classes = (IsAuthenticated,)


class CategoryDiscussions(APIView):
    def get(self, request, category_id):
        vacancies = Discussion.objects.filter(category_id=category_id)
        serializer = DiscussionSerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},status = status.HTTP_500_INTERNAL_SERVER_ERROR)
