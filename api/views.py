from rest_framework import viewsets, views, status, parsers
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Publicacao, Comentario
from .serializers import UsuarioSerializer, PublicacaoSerializer, ComentarioSerializer
from .permissions import ReadOnlyOrIsAuthenticated, IsOwnerOrStaff


@extend_schema(tags=["autenticação"])
class LoginView(TokenObtainPairView):
    pass


class SignupView(views.APIView):
    @extend_schema(
        tags=["autenticação"],
        request=UsuarioSerializer,
        responses={status.HTTP_201_CREATED: UsuarioSerializer}
    )
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicacaoViewSet(viewsets.ModelViewSet):
    queryset = Publicacao.objects.all()
    serializer_class = PublicacaoSerializer
    permission_classes = [ReadOnlyOrIsAuthenticated, IsOwnerOrStaff]
    parser_classes = [parsers.MultiPartParser]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        publicacao = self.get_object()
        comentarios = Comentario.objects.filter(publicacao=publicacao)
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [ReadOnlyOrIsAuthenticated, IsOwnerOrStaff]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
