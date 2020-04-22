from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300, default='name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Discussion(models.Model):
    name = models.CharField(max_length=300, default='name')
    description = models.TextField(default='')
    topics_count = models.FloatField(default=0)
    posts_count = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='discussions')

    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussions'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'topics_count': self.topics_count,
            'posts_count': self.posts_count,
            'category': self.category_id
        }


class Topic(models.Model):
    unread = models.FloatField(default=4)
    title = models.CharField(max_length=300, default='title')
    description = models.TextField(default='')
    author = models.TextField(default='author')
    date = models.DateField(default='February 4, 2016 10:13:00')
    replies = models.FloatField(default=4)
    views = models.FloatField(default=201)
    last_author = models.TextField(default='last author')
    last_date = models.DateField(default='April 17, 2020 11:17:00')
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE,
                                   related_name='topics')

    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    def to_json(self):
        return {
            'id': self.id,
            'unread': self.unread,
            'title': self.title,
            'description': self.description,
            'author': self.author,
            'date': self.date,
            'replies': self.replies,
            'views': self.views,
            'last_author': self.last_author,
            'last_date': self.last_date,
            'discussion': self.discussion_id,
        }


class Comment(models.Model):
    content = models.TextField(default='')
    author = models.TextField(default='author')
    date = models.DateField(default='May 2, 2016 10:13:00')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,
                              related_name='comments')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'author': self.author,
            'date': self.date,
            'topic': self.topic_id,
        }