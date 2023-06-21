# Third party
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# DRF
from rest_framework.routers import DefaultRouter

# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path
)

# First party
from main import views


router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
urlpatterns = [
    path(settings.ADMIN_PAGE_URL, admin.site.urls),
    path('simple', views.simple),
    path('test_performance', views.test_performance),
    path('', views.index),
    #
    path('api/v1/', include(router.urls)),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),  # noqa: E501
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
