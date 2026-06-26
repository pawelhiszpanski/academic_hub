from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=150)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.abbreviation})"


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="field_of_study")

    def __str__(self):
        return f"{self.name} - {self.faculty.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30, unique=True) # eg. ETI-INF-2026
    semester = models.IntegerField()
    field_of_study = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return f"{self.name} (Semester: {self.semester} - {self.field_of_study.name})"

