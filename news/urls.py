from django.urls import path

# from .views import NewsList, NewsDetail, UserList, UserDetail

# urlpatterns = [
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('<int:pk>/', NewsDetail.as_view()),
#     path('', NewsList.as_view()),
# ]

from rest_framework.routers import SimpleRouter
from .views import UserViewSet, NewsViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', NewsViewSet, basename='news')

urlpatterns = router.urls