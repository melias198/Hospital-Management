from django.db import models

# Create your models here.
class Patient(models.Model):
    record_id = models.IntegerField()
    patient_id = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.CharField(max_length=200)
    observations = models.CharField(max_length=300)
    treatments = models.CharField(max_length=300)
    department_id = None
    misc = models.CharField(max_length=300)
    
    def __str__(self):
        return self.diagnostics
    