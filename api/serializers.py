from rest_framework import serializers
from .models import Usuario, Publicacao, Comentario


class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'username', 'nome', 'senha')

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        usuario = Usuario.objects.create_user(password=senha, **validated_data)
        return usuario


class PublicacaoSerializer(serializers.ModelSerializer):
    autor = UsuarioSerializer(read_only=True)
    publicado_em = serializers.CharField(read_only=True)
    imagem = serializers.ImageField(required=False)

    class Meta:
        model = Publicacao
        fields = ['id', 'titulo', 'imagem', 'descricao',
                  'autor', 'publicado_em']


class ComentarioSerializer(serializers.ModelSerializer):
    autor = UsuarioSerializer(read_only=True)

    class Meta:
        model = Comentario
        fields = ['id', 'autor',
                  'publicacao', 'mensagem', 'publicado_em']
