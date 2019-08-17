from django.urls import path
from blogging.views import stub_view, list_view, detail_view
from blogging.feeds import LatestPostsFeed

from django.urls import include, path
from rest_framework import routers
from blogging import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
    path('latest/feed/', LatestPostsFeed()),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
