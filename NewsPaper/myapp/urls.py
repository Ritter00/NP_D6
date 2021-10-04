from django.urls import path
from .views import PostList, PostDetail, PostListSearch, PostCreateView, PostUpdateView, PostDeleteView
from .views import upgrade_me, CategoryList, CategoryDetail, subscriber, is_subscriber

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostListSearch.as_view()),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateView.as_view(),name='post_update' ),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('create/upgrade/', upgrade_me, name='upgrade'),
    path('category/', CategoryList.as_view(), name='categories' ),
    path('category/<int:pk>', CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>', subscriber, name='subscriber'),
    path('category/<int:pk>', is_subscriber, name='is_subscriber'),

    ]