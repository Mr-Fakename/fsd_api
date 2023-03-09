from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ObtainTokenView, RegisterView, mongo_call, SetupView, TokenRefreshView

router = DefaultRouter()
router.register('setup', SetupView, basename='setup')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', ObtainTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('mongo/', mongo_call, name='mongo_call'),
]
