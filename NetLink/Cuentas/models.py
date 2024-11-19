from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Experience(models.Model):
    company = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    description = models.CharField(max_length=256)
    def getCompany(self):
        return self.company
    def setCompany(self, company):
        self.company = company
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description

class laboralInformation(models.Model):
    latestPosition = models.ForeignKey('Experience', on_delete=models.CASCADE, related_name='+')
    abilities = ArrayField(models.CharField(max_length=30), blank=True)
    previousExperiences = models.ManyToManyField(Experience)
    lookingForEmployement = models.BooleanField()
    desiredPosition = models.CharField(max_length=30)
    desiredCountry = models.CharField(max_length=30)
    telecommuting = models.BooleanField()
    def getLatestPosition(self):
        return self.latestPosition
    
    def setLatestPosition(self, company, position, description):
        self.latestPosition = Experience(company, position, description)
    
    def getAbilities(self):
        return self.abilities
    
    def setAbilities(self, ability):
        self.abilities.append(ability)
    
    def getPreviousExperiences(self):
        return self.previousExperiences
    
    def setPreviousExperiences(self, company, position, description):
        newExperience = Experience(company, position, description)
        self.previousExperiences.append(newExperience)
    
    def getLookingForEmployement(self):
        return self.lookingForEmployement
    
    def setLookingForEmployement(self, isLooking):
        self.lookingForEmployement = isLooking
    
    def getDesiredPosition(self):
        return self.desiredPosition
    
    def setDesiredPosition(self, desiredPosition):
        self.desiredPosition = desiredPosition
    
    def getDesiredCountry(self):
        return self.desiredCountry
    
    def setDesiredCountry(self, desiredCountry):
        self.desiredCountry = desiredCountry
    
    def getTelecommuting(self):
        return self.telecommuting
    
    def setTelecommuting(self, telecommuting):
        self.telecommuting = telecommuting
    
    def addExperience(self, company, position, description):
        newExperience = Experience(company, position, description)
        self.previousExperiences.add(newExperience)
        return self.previousExperiences
    
    def addAbility(self, ability):
        self.abilities.append(ability)
        return self.abilities

class AcademicInformation(models.Model):
    educativeInstitution = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    academicDiscipline = models.CharField(max_length=30)
    startDate = models.DateField(max_length=10)
    endDate = models.DateField(max_length=10)
    aditionalActivities = ArrayField(models.CharField(max_length=100), blank=True)
    description = models.CharField(max_length=30)
    abilities= ArrayField(models.CharField(max_length=100), blank=True)
    
    def getEducativeInstitution(self):
        return self.educativeInstitution
    
    def setEducativeInstitution(self, educativeInstitution):
        self.educativeInstitution = educativeInstitution
    
    def getTitle(self):
        return self.title
    
    def setTitle(self, title):
        self.title = title
    
    def getAcademicDiscipline(self):
        return self.academicDiscipline
    
    def setAcademicDiscipline(self, academicDiscipline):
        self.academicDiscipline = academicDiscipline
    
    def getStartDate(self):
        return self.startDate
    
    def setStartDate(self, startDate):
        self.startDate = startDate
    
    def getEndDate(self):
        return self.endDate
    
    def setEndDate(self, endDate):
        self.endDate = endDate
    
    def getAbilities(self):
        return self.abilities
    
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description
    
    def getAditionalActivities(self):
        return self.aditionalActivities
    
    def addAditionalActivity(self, activity):
        self.aditionalActivities.append(activity)
        return self.aditionalActivities
    
    def addAbility(self, ability):
        self.abilities.append(ability)
        return self.abilities



class Usuario(models.Model):
    nombre=models.CharField(max_length=200)
    contrasena=models.CharField(max_length=30)
    fechaNacimiento=models.DateField()
    email=models.CharField(max_length=100)
    paisOrigen=models.CharField(max_length=30)


    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getAbilities(self):
        return self.nombre
    
    def setContrasena(self, contrasena):
        self.contrasena = contrasena
    
    def getContrasena(self):
        return self.contrasena 
    
    def setFechaNacimiento(self, fechaNacimiento):
        self.fechaNacimiento = fechaNacimiento
    
    def getFechaNacimiento(self):
        return self.fechaNacimiento
    
    def setEmail(self, email):
        self.email = email
    
    def getEmail(self):
        return self.email
    
    def setPaisOrigen(self, paisOrigen):
        self.paisOrigen = paisOrigen
    
    def getPaisOrigen(self):
        return self.paisOrigen