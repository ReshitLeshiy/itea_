from django.db import models
from django.utils import timezone

# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.role}"

    class Meta:
        db_table = 'Role'

class Vacancy(models.Model):
    title_tk = models.CharField(max_length=255, null=False, blank=False)
    title_ru = models.CharField(max_length=255, null=False, blank=False)
    title_en = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to='photos/', blank=False, null=False)
    description_tk = models.TextField(null=False, blank=False)
    description_ru = models.TextField(null=False, blank=False)
    description_en = models.TextField(null=False, blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'Vacancy'

class News(models.Model):
    title_tk = models.CharField(max_length=255, blank=False, null=False)
    title_ru = models.CharField(max_length=255, blank=False, null=False)
    title_en = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='photos/', blank=False, null=False)
    content_tk = models.TextField(blank=False, null= False)
    content_ru = models.TextField(blank=False, null=False)
    content_en = models.TextField(blank=False, null=False)
    date_published = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'News'

class Team(models.Model):
    full_name_tk = models.CharField(max_length=200, blank=False, null=False)
    full_name_ru = models.CharField(max_length=200, blank=False, null=False)
    full_name_en = models.CharField(max_length=200, blank=False, null=False)
    photo = models.ImageField(upload_to='photos/', blank=False, null=False)
    position = models.ForeignKey(to=Role, on_delete=models.SET_NULL, blank=True, null=True)
    activity_tk = models.TextField(blank=True, null=True)
    activity_ru = models.TextField(blank=True, null=True)
    activity_en = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'Team'

    def __str__(self):
        return f"{self.full_name_tk}, {self.full_name_ru}, {self.full_name_en}"


class Course(models.Model):
    name_en = models.CharField(max_length=255, blank=False, null=False)
    description_tk = models.TextField(blank=False, null=False)
    description_ru = models.TextField(blank=False, null=False)
    description_en = models.TextField(blank=False, null=False)
    duration = models.IntegerField(blank=False, null=False)
    topics_tk = models.TextField(blank=True, null=True)
    topics_ru = models.TextField(blank=True, null=True)
    topics_en = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        db_table = 'Course'

    def __str__(self):
        return f"{self.name_en}, {self.duration}, {self.is_active}"

class User(models.Model):
    full_name = models.CharField(max_length=255, blank=False, null=False)
    phone_number = models.CharField(max_length=50, blank=False, null=False)
    courses = models.ManyToManyField(Course, blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(blank=False, null=False, default=True)

    class Meta:
        db_table = 'Users'

    def __str__(self):
        return f"{self.full_name}"

class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        unique_together = [['user', 'course']]

    def __str__(self):
        return f"{self.user.full_name} - {self.course.name_en}: {self.points} points"






