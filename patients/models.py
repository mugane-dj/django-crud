from django.db import models

class Gender(models.Model):
    gender_form = models.CharField(max_length=15)

    def __str__(self):
        return self.gender_form

class Blood(models.Model):
    blood_form = models.CharField(max_length=50)

    def __str__(self):
        return self.blood_form

class Surgery(models.Model):
    surgery_form = models.CharField(max_length=15)

    def __str__(self):
        return self.surgery_form

class Patient(models.Model):
    fullname = models.CharField(max_length=100)
    patient_code = models.CharField(max_length=4)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    blood_group = models.ForeignKey(Blood, on_delete=models.CASCADE)
    surgery = models.ForeignKey(Surgery, on_delete=models.CASCADE)
    next_of_kin_name = models.CharField(max_length=100)
    next_of_kin_contact = models.CharField(max_length=15)
    medical_allergies = models.TextField(blank=False)
    

