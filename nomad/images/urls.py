from django.urls import path
from . import views

app_name = "images"

urlpatterns = [
    path(
        #all로 이동
        "feed/",
        view = views.Feed.as_view(),
        name = 'all image'
    ),
    
    # test codes
    
    # path(
    #     #all로 이동
    #     "all/",
    #     view = views.ListAllImages.as_view(),
    #     name = 'all image'
    # ),
    # path(
    #     #all로 이동
    #     "comments/",
    #     view = views.ListAllComments.as_view(),
    #     name = 'all image'
    # ),
    # path(
    #     #all로 이동
    #     "likes/",
    #     view = views.ListAllLikes.as_view(),
    #     name = 'all image'
    # ),
]
