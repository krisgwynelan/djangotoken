from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import SecureHelloView
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Your task-related endpoints
    path('secure-hello/', SecureHelloView.as_view(), name='secure-hello'),  # Your authenticated endpoint
    path('api-token-auth/', obtain_auth_token),  # Endpoint for obtaining tokens
]
