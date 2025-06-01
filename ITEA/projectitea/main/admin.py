from django.contrib import admin
from django.utils.html import format_html
from .models import Role, Vacancy, Team, News, Course, User, UserCourse


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['id', 'role']
    search_fields = ['role']

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_tk', 'title_ru', 'title_en', 'image', 'description_tk', 'description_ru', 'description_en', 'date_posted', 'is_active']
    search_fields = ['title_tk', 'title_ru', 'title_en', 'date_posted']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_tk', 'title_ru', 'title_en', 'image', 'content_tk', 'content_ru', 'content_en', 'date_published', 'is_active']
    search_fields = ['title_ru', 'title_en', 'title_tk', 'date_published']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name_tk', 'full_name_ru', 'full_name_en', 'photo', 'position', 'activity_tk', 'date', 'is_active']
    search_fields = ['full_name_tk', 'full_name_ru', 'full_name_en', 'date']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_en', 'description_tk', 'description_en', 'description_ru', 'date', 'is_active']
    search_fields = ['name_en', 'date']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone_number', 'registration_date', 'is_active']
    search_fields = ['full_name']
    filter_horizontal = ('courses',)


@admin.register(UserCourse)
class UserCourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'points']
    search_fields = ['user']