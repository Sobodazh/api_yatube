from rest_framework.authtoken import views
from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, UserViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(r'users', UserViewSet, basename='users')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
