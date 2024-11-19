from Cuentas.models import Experience, laboralInformation, AcademicInformation, Usuario
from rest_framework import serializers
from rest_framework.utils import html, model_meta, representation

class experienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields =('id','company', 'position', 'description')

class laboralInformationSerializer(serializers.ModelSerializer):
    latestPosition = experienceSerializer()
    previousExperiences = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Experience.objects.all(), required=False  # Hacer que no sea obligatorio
    )
    
    class Meta:
        model = laboralInformation
        fields = ('id', 'latestPosition', 'abilities', 'previousExperiences', 'lookingForEmployement', 'desiredPosition', 'desiredCountry', 'telecommuting')

    def create(self, validated_data):
        latest_position_data = validated_data.pop('latestPosition')
        previous_experiences= validated_data.pop('previousExperiences', [])
        
        latest_position = Experience.objects.create(**latest_position_data)
        
        laboral_info = laboralInformation.objects.create(latestPosition=latest_position, **validated_data)
        
        laboral_info.previousExperiences.set(previous_experiences)
        laboral_info.save()
        
        return laboral_info
    
    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                try:
                    setattr(instance, attr, value)
                except ValueError:
                    if validated_data.get("latestPosition").get("company") != instance.getLatestPosition().getCompany() or validated_data.get("latestPosition").get("position") != instance.getLatestPosition().getPosition() and validated_data.get("latestPosition").get("description") != instance.getLatestPosition().getDescrpition():
                        experience =Experience.objects.create(company=validated_data.get("latestPosition").get("company"),
                        position= validated_data.get("latestPosition").get("position"),
                        description= validated_data.get("latestPosition").get("description"))
                        setattr(instance, attr, experience)
                    else:
                        setattr(instance, attr, instance.getLatestPosition())

        instance.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance
    
class academicInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicInformation
        fields =('id', 'educativeInstitution', 'title','academicDiscipline','startDate', 'endDate','aditionalActivities', 'description','abilities')

class usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields=[
            'id',
            'nombre',
            'contrasena',
            'fechaNacimiento',
            'email',
            'paisOrigen'
        ]
