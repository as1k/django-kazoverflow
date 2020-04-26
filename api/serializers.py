from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category, Discussion, Topic, Comment


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password',)

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        category = Category.objects.create(name=validated_data.get('name'))
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class DiscussionSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'name', 'description', 'topics_count', 'posts_count', 'category_id',)


class CategoryWithDiscussionsSerializer(serializers.ModelSerializer):
    discussions = DiscussionSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'discussions')


class TopicSerializer(serializers.ModelSerializer):
    discussion_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'unread', 'title', 'description', 'author', 'date', 'replies',
                  'views', 'last_author', 'last_date', 'discussion_id')


class CommentMSerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'date', 'topic_id')


class DiscussionWithTopicsSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = ('id', 'name', 'description', 'topics_count', 'posts_count', 'category_id', 'topics')


class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    author = serializers.CharField()
    date = serializers.DateField()
    topic_id = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        comment = Comment.objects.create(content=validated_data('content'),
                                         author=validated_data('author'),
                                         date=validated_data('date'),
                                         topic_id=validated_data('topic_id'))
        return comment

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.date = validated_data.get('date', instance.date)
        instance.topic_id = validated_data.get('topic_id', instance.topic_id)
        instance.save()
        return instance


class TopicWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'unread', 'title', 'description', 'author', 'date', 'replies',
                  'views', 'last_author', 'last_date', 'discussion_id', 'comments')
