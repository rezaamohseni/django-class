from django.urls import path
from .views import *

app_name = "services-api"

urlpatterns = [
    path(
        "services",
        ServiceApiViewSet.as_view({"get": "list", "post": "create"}),
        name="services",
    ),
    path(
        "services/<int:pk>",
        ServiceApiViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="services_detail",
    ),
    path(
        "team", TeamApiViewSet.as_view({"get": "list", "post": "create"}), name="team"
    ),
    path(
        "team/<int:pk>",
        TeamApiViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="team-detail",
    ),
    path(
        "comment",
        CommentApiViewSet.as_view({"get": "list", "post": "create"}),
        name="comment",
    ),
    path(
        "comment/<int:pk>",
        CommentApiViewSet.as_view(
            {"get": "retrieve", "patch": "update", "delete": "destroy"}
        ),
        name="comment-detail",
    ),
]

# urlpatterns = [
#     path('services' , ServiceApiViewSet.as_view() , name='services'),
#     path('services/<int:pk>' , ServiceApiViewSet.as_view() , name='services_detail')
# ]
