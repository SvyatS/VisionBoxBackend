from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView,
)

from .yasg import urlpatterns as doc_urls
from users.views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('projects.urls')),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += doc_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)