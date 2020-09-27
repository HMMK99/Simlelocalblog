from django.urls import path

from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
	path('posty/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
	path('posty/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
	path('posty/new/', BlogCreateView.as_view(), name='post_new'),
	path('posty/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
	path('', BlogListView.as_view(), name='home'),
]
