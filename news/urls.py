from django.urls import path

from .views import NewsList, NewsDetail

urlpatterns = [
    path('<int:pk>/', NewsDetail.as_view()),
    path('', NewsList.as_view()),
]