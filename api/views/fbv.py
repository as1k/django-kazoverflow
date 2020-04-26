from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from api.models import Category, Discussion, Topic, Comment
from api.serializers import CategorySerializer, \
    DiscussionSerializer, TopicSerializer, \
    CommentSerializer, CategoryWithDiscussionsSerializer, \
    DiscussionWithTopicsSerializer, TopicWithCommentsSerializer, \
    CommentMSerializer, UserSerializer


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategoryWithDiscussionsSerializer(categories, many=True)
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
        serializer = CategoryWithDiscussionsSerializer(category)
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


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def category_discussions(request, category_id):
    try:
        # category = Category.objects.get(id=category_id)
        discussions = Discussion.objects.filter(category_id=category_id)
    except (Category.DoesNotExist or Discussion.DoesNotExist) as e:
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
def topic_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 4
        topics = Topic.objects.all()
        result_page = paginator.paginate_queryset(topics, request)
        serializer = TopicSerializer(result_page, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
# @permission_classes([IsAuthenticated])
def topic_detail(request, topic_id):
    try:
        topic = Topic.objects.get(id=topic_id)
    except Topic.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = TopicWithCommentsSerializer(topic)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TopicSerializer(instance=topic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        topic.delete()
        return Response({'deleted': True})

    elif request.method == 'POST':
        serializer = CommentMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def discussion_topics(request, discussion_id):
    try:
        discussion = Discussion.objects.get(id=discussion_id)
        # topics = Topic.objects.filter(discussion_id=discussion_id) # default
        topics = Topic.sorted_objects.sort_by_title(request).filter(discussion_id=discussion_id) # sort by title
        # topics = Topic.sorted_objects.sort_by_id(request).filter(discussion_id=discussion_id) # sort by id
    except (Category.DoesNotExist or Discussion.DoesNotExist or Topic.DoesNotExist) as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(topics, request)
        serializer = TopicSerializer(result_page, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TopicSerializer(instance=topics, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        topics.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def comment_detail(request, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
    except Comment.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        comment.delete()
        return Response({'deleted': True})


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def topic_comments(request, category_id, discussion_id, topic_id):
    try:
        # category = Category.objects.get(id=category_id)
        # discussion = Discussion.objects.get(id=discussion_id)
        # topic = Topic.objects.get(id=topic_id)
        comments = Comment.objects.filter(topic_id=topic_id)
    except (Category.DoesNotExist or Discussion.DoesNotExist or Topic.DoesNotExist or Comment.DoesNotExist) as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(instance=comments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        comments.delete()
        return Response({'deleted': True})


@api_view(['POST'])
@permission_classes((AllowAny,))
def create_user(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
