from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import PublicacaoViewSet, ComentarioViewSet, SignupView, LoginView

router = routers.DefaultRouter()
router.register(r'publicacao', PublicacaoViewSet)
router.register(r'comentario', ComentarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/doc/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),

    path('cadastrar/', SignupView.as_view(), name='sign-up'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
]
