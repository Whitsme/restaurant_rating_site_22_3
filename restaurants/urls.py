from django.urls import path
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', ReviewListView.as_view(), name='home'), 
    path('restaurants/review/<int:pk>/', ReviewDetailView.as_view(), name='r_r_details'),
    path('restaurants/review/new/', ReviewCreateView.as_view(), name='r_r_new'),
    path('restaurants/review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='r_r_edit'),
    path('restaurants/review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='r_r_delete'),
]
