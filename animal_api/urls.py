from django.urls import path, include
from rest_framework.authtoken import views as authview
from rest_framework.routers import DefaultRouter
from .views import AnimalViewSet

router = DefaultRouter()
router.register('animals', AnimalViewSet)

urlpatterns = [
    path('token/', authview.obtain_auth_token, name='api_token_auth'),
    path('', include(router.urls))
]
