from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, HubPostListView, MarketListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', PostListView.as_view(), name='hubbleHome'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('item/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
    path('market/', MarketListView.as_view(), name='hubbleMarket'),
    path('hub/<str:university>', HubPostListView.as_view(), name='hub'),
    path('hub/University of Lincoln/', HubPostListView.as_view(), name='hubbleLincoln'),
    path('hull/', views.hull, name='hubbleHull'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)