from django.shortcuts import render
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from Cuentas.models import laboralInformation
from django.db import models
from Cuentas.models import Experience, AcademicInformation, Usuario
from Cuentas.serializer import laboralInformationSerializer, academicInformationSerializer, experienceSerializer, usuario_serializer

class experienceApiView(APIView):
    def get(self, request, *args, **kwargs):
        eList = Experience.objects.all()
        eSerializer = experienceSerializer(eList, many=True)
        return Response(eSerializer.data, status=status.HTTP_200_OK)
    
    def getExperience(self, request, id, *args, **kwargs):
        miExperience = Experience.objects.filter(id = id).first()
        eSerializer = experienceSerializer(miExperience, many=True)
        return Response(eSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        
        data = {
            'company':request.data.get('company'),
            'position': request.data.get('position'),
            'description': request.data.get('description')
        }
        
        serializer = experienceSerializer(data=data)
        
        if serializer.is_valid():
            experience = serializer.save()
            experience.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid, *args, **kwargs):
        try:
            experience = Experience.objects.get(id=pkid)
        except Experience.DoesNotExist:
            return Response({'error': 'Vehículo no encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = experienceSerializer(experience, data=request.data, partial=True) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pkid):
        try:
            experience = Experience.objects.get(id=pkid)
            
            experience.delete()
            
            return Response({"message": "Información laboral eliminada exitosamente."}, status=status.HTTP_200_OK)
        
        except Experience.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)


class laboralInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        laboralList = laboralInformation.objects.all()
        laboralSerializer = laboralInformationSerializer(laboralList, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def getLaboralInfo(self, request, id, *args, **kwargs):
        miLaboralInfo = laboralInformation.objects.filter(id = id).first()
        laboralSerializer = laboralInformationSerializer(miLaboralInfo, many=True)
        return Response(laboralSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        previousExperiences = []
        
        for i in request.data.get('previousExperiences'):
            experience = Experience.objects.create(company=i['company'],
                position= i['position'],
                description= i['description'])

            previousExperiences.append(experience.pk)
        
        data = {
            'latestPosition':request.data.get('latestPosition'),
            'abilities': request.data.get('abilities'),
            'previousExperiences': previousExperiences,
            'lookingForEmployement': request.data.get('lookingForEmployement'),
            'desiredPosition': request.data.get('desiredPosition'),
            'desiredCountry': request.data.get('desiredCountry'),
            'telecommuting': request.data.get('telecommuting')
        }
        
        serializer = laboralInformationSerializer(data=data)
        print(request.data)
        if serializer.is_valid():
            laboral_info = serializer.save()
            laboral_info.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pkid, *args, **kwargs):
        try:
            laboral = laboralInformation.objects.get(id=pkid)
        except laboralInformation.DoesNotExist:
            return Response({'error': 'Informacion no encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        previousExperiences = []
        abilities = laboral.abilities
        
        for i in laboral.previousExperiences.values_list():
            previousExperiences.append(i[0])
        
        
        for i in request.data.get('abilities'):
            abilities.append(i)
        
        for i in request.data.get('previousExperiences'):
            experience = Experience.objects.create(company=i['company'],
                position= i['position'],
                description= i['description'])

            previousExperiences.append(experience.pk)
        
        data = {
            'latestPosition':request.data.get('latestPosition'),
            'abilities': abilities,
            'previousExperiences': previousExperiences,
            'lookingForEmployement': request.data.get('lookingForEmployement'),
            'desiredPosition': request.data.get('desiredPosition'),
            'desiredCountry': request.data.get('desiredCountry'),
            'telecommuting': request.data.get('telecommuting')
        }
                
        serializer = laboralInformationSerializer(laboral,data=data, partial=True) 
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(request.data)
        print(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pkid):
        try:
            laboral_info = laboralInformation.objects.get(id=pkid)
            
            laboral_info.delete()
            
            return Response({"message": "Información laboral eliminada exitosamente."}, status=status.HTTP_200_OK)
        
        except laboralInformation.DoesNotExist:
            return Response({"error": "Información laboral no encontrada."}, status=status.HTTP_404_NOT_FOUND)


class academicInformationApiView(APIView):
    def get(self, request, *args, **kwargs):
        academicList = AcademicInformation.objects.all()
        academicSerializer = academicInformationSerializer(academicList, many=True)
        return Response(academicSerializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'educativeInstitution': request.data.get('educativeInstitution'),
            'title': request.data.get('title'),
            'academicDiscipline': request.data.get('academicDiscipline'),
            'startDate': request.data.get('startDate'),
            'endDate': request.data.get('endDate'),
            'aditionalActivities': request.data.get('aditionalActivities'),
            'description': request.data.get('description'),
            'abilities': request.data.get('abilities')
        }
        
        serializer = academicInformationSerializer(data=data)
        
        if serializer.is_valid():
            academic_info = serializer.save()
            
            academic_info.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pkid):
        try:
            academic_info = AcademicInformation.objects.get(id=pkid)
            
            academic_info.delete()
            
            return Response({"message": "Información académica eliminada exitosamente."}, status=status.HTTP_200_OK)
        
        except AcademicInformation.DoesNotExist:
            return Response({"error": "Información académica no encontrada."}, status=status.HTTP_404_NOT_FOUND)
        

class UsuariosView(APIView):
    def get(self, request, *args, **kwargs):
            lista_usuarios=Usuario.objects.all()
            serializer_usuarios=usuario_serializer(lista_usuarios, many=True)
            return Response(serializer_usuarios.data,status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        data = {
            'nombre': request.data.get('nombre'),
            'contrasena': request.data.get('contrasena'),
            'fechaNacimiento': request.data.get('fechaNacimiento'),
            'email': request.data.get('email'),
            'paisOrigen': request.data.get('paisOrigen')       
        }

        serializador = usuario_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(
                {"message": "Usuario creado correctamente", "data": serializador.data},
                status=status.HTTP_201_CREATED
            )
    
        return Response(
            {"message": "El usuario no se pudo crear", "errors": serializador.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pkid):
    # Intenta actualizar el usuario y guarda la cantidad de registros afectados
        registros_actualizados = Usuario.objects.filter(id=pkid).update(
            nombre=request.data.get('nombre'),
            contrasena=request.data.get('contrasena'),
            fechaNacimiento=request.data.get('fechaNacimiento'),
            email=request.data.get('email'),
            paisOrigen=request.data.get('paisOrigen')
        )

    # Si se actualizó al menos un registro, devuelve un mensaje de éxito
        if registros_actualizados > 0:
            return Response(
                {"message": "Usuario actualizado correctamente"},
                status=status.HTTP_200_OK
        )
        else:
            return Response(
                {"message": "El usuario no se pudo actualizar"},
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def delete(self, request, pkid, *args, **kwargs):
        try:
            usuario = Usuario.objects.get(id=pkid)
            usuario.delete()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)
        except Usuario.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
          
class UsuarioQueryApiView(APIView):
    def get(self, request, pkid, *args, **kargs):
        miUsuario=Usuario.objects.filter(id=pkid).first()
        serializer_usuario = usuario_serializer(miUsuario)
        return Response(serializer_usuario.data, status=status.HTTP_200_OK)

class validateApiView(APIView):
    def post(self, request, *args, **kwargs):
        data={
            'email':request.data.get('email'),
            'contrasena':request.data.get('contrasena'),
        }
        if Usuario.objects.filter(email=data['email'], contrasena=data['contrasena']).exists():
            return Response(True, status=status.HTTP_200_OK) #ver perfil
        return Response(False, status=status.HTTP_400_BAD_REQUEST)

