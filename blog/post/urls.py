from django.urls import path
from .views import IndexView, PostDetailView, PostCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index_by_class'),
    path('post/<int:post_id>/', PostDetailView.as_view(), name='post_detail_by_class'),
    path('post/create/', PostCreateView.as_view(), name='post_create_by_class'),
]
