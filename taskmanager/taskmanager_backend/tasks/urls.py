from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('auth/token/', obtain_jwt_token),
]
