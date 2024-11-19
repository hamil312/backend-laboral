from rest_framework import serializers
from api_publicacion.models import publicacion

class publicacion_serializer(serializers.ModelSerializer):
    class Meta:
        model = publicacion
        fields = ['id', 'titulo', 'descripcion', 'multimedia', 'date_created']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['date_created'] = instance.date_created.strftime('%Y-%m-%d %H:%M:%S')
        return data