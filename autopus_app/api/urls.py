from django.urls import path, include
from autopus_app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('crud', views.ProductViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls))
]
