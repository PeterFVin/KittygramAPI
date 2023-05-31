from django.urls import include, path

from rest_framework.routers import DefaultRouter

from cats.views import CatViewSet, LightCatViewSet, OwnerViewSet


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register(r'mycats', LightCatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('auth/', include('djoser.urls.jwt')),
]
