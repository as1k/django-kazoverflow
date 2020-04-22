from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views.cbv import CategoryList, CategoryDetails, DiscussionList, DiscussionDetails, CategoryDiscussions, \
    TopicList, TopicDetails, DiscussionTopics

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),
    path('discussions/', DiscussionList.as_view()),
    path('discussions/<int:pk>/', DiscussionDetails.as_view()),
    path('categories/<int:category_id>/discussions/', CategoryDiscussions.as_view()),
    path('topics/', TopicList.as_view()),
    path('topics/<int:pk>/', TopicDetails.as_view()),
    path('categories/<int:category_id>/discussions/<int:discussion_id>/topics/', DiscussionTopics.as_view()),
]