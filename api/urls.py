from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views.fbv import category_list, category_detail, discussion_list, discussion_detail, category_discussions, \
    topic_list, topic_detail, discussion_topics, comment_list, comment_detail, topic_comments
from api.views.cbv import CategoryList, CategoryDetails, DiscussionList, DiscussionDetails, CategoryDiscussions, \
    TopicList, TopicDetails, DiscussionTopics, CommentList, CommentDetails, TopicComments

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('categories/', category_list),
    path('categories/<int:category_id>/', category_detail),
    path('discussions/', discussion_list),
    path('discussions/<int:discussion_id>', discussion_detail),
    path('categories/<int:category_id>/discussions/', category_discussions),
    path('topics/', topic_list),
    path('topics/<int:topic_id>/', topic_detail),
    path('discussions/<int:discussion_id>/topics/', discussion_topics),
    path('comments/', comment_list),
    path('comments/<int:comment_id>/', comment_detail),
    path('categories/<int:category_id>/discussions/<int:discussion_id>/topics/<int:topic_id>/comments/', topic_comments)
]


# urlpatterns = [
#     path('login/', obtain_jwt_token),
#     path('categories/', CategoryList.as_view()),
#     path('categories/<int:pk>/', CategoryDetails.as_view()),
#     path('discussions/', DiscussionList.as_view()),
#     path('discussions/<int:pk>/', DiscussionDetails.as_view()),
#     path('categories/<int:category_id>/discussions/', CategoryDiscussions.as_view()),
#     path('topics/', TopicList.as_view()),
#     path('topics/<int:pk>/', TopicDetails.as_view()),
#     path('categories/<int:category_id>/discussions/<int:discussion_id>/topics/', DiscussionTopics.as_view()),
#     path('comments/', CommentList.as_view()),
#     path('comments/<int:pk>/', CommentDetails.as_view()),
#     path('categories/<int:category_id>/discussions/<int:discussion_id>/topics/<int:topic_id>/comments/', TopicComments.as_view())
# ]
