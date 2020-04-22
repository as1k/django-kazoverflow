from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api.views.cbv import CategoryList, CategoryDetails, DiscussionList, DiscussionDetails, CategoryDiscussions

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetails.as_view()),
    path('discussions/', DiscussionList.as_view()),
    path('discussions/<int:pk>/', DiscussionDetails.as_view()),
    path('categories/<int:category_id>/discussions/', CategoryDiscussions.as_view())
]