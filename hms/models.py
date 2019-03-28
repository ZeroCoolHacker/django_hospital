from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=50)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name



class Reciept(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description = models.TextField('Description', blank=True)
    reciept = models.ImageField(upload_to='reciepts', blank=True)

    def __str__(self):
        return self.patient.name