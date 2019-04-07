from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, HubPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='hubbleHome'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('market/', views.market, name='hubbleMarket'),
    path('hub/<str:university>', HubPostListView.as_view(), name='hub'),
    path('hull/', views.hull, name='hubbleHull'),
]
