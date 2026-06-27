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

    STREAM_CHOICES = [
        ('ALL', 'Wspólny'),
        ('APP', 'Aplikacje'),
        ('SYS', 'Systemy'),
    ]

    stream = models.CharField(
        max_length=3,
        choices=STREAM_CHOICES,
        default='ALL'
    )

    def __str__(self):
        return f"{self.name} (Semester: {self.semester} - {self.field_of_study.name})"


class Resource(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    RESOURCE_CHOICES = [
        ('LEC', 'Wykład'),
        ('LAB', 'Laboratorium'),
        ('PROJ', 'Projekt')
    ]

    resource_type = models.CharField(
        max_length=4,
        choices=RESOURCE_CHOICES,
        default='LEC'
    )

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="resources")

    def __str__(self):
        return f"{self.title} ({self.resource_type})"