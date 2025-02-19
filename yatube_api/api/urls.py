from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedDefaultRouter

from .views import PostViewSet, GroupViewSet, FollowViewSet, CommentViewSet


router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("follow", FollowViewSet)
router.register("groups", GroupViewSet)

comments_router = NestedDefaultRouter(router, "posts", lookup="post")
comments_router.register("comments", CommentViewSet, basename="post-comments")


urlpatterns = [
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
    path("v1/", include(router.urls)),
    path("v1/", include(comments_router.urls)),
]
