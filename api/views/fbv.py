from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.models import Category, Discussion, Topic, Comment
from api.serializers import CategorySerializer, DiscussionSerializer, TopicSerializer, CommentSerializer


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def category_detail(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        category.delete()
        return Response({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def category_discussions(request, category_id):
    try:
        discussions = Discussion.objects.filter(category_id=category_id)
    except Discussion.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiscussionSerializer(instance=discussions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        discussions.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def discussion_list(request):
    if request.method == 'GET':
        discussions = Discussion.objects.all()
        serializer = DiscussionSerializer(discussions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiscussionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def discussion_detail(request, discussion_id):
    try:
        discussion = Discussion.objects.get(id=discussion_id)
    except Discussion.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = DiscussionSerializer(discussion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiscussionSerializer(instance=discussion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        discussion.delete()
        return Response({'deleted': True})
