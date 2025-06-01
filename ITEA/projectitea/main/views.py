from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import LoginForm
from .models import *
from .serializers import *
from django.shortcuts import redirect, get_object_or_404, get_list_or_404


#?id=1&lang=ru

@api_view(['GET'])
def index(request):
    lang = request.GET.get('lang', 'ru')
    t = Team.objects.all()
    t = t[:10]
    t_serializer = TeamSerializer(t, many=True)
    c = Course.objects.all()
    c = c[:3]
    c_serializer = CourseSerializer(c, many=True)
    context = {
        'team': t_serializer.data,
        'course': c_serializer.data,
        'lang': lang
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
def news(request):
    article = request.GET.get('article', None) #вернет строку 
    lang = request.GET.get('lang', 'ru')
    if article:    
        a = get_object_or_404(News, id=int(article))
        serializer = NewsSerializer(a)
        return Response(serializer.data, status=status.HTTP_200_OK)
    items = News.objects.all()
    serializer = NewsSerializer(items, many=True)
    context = {
        'data': serializer.data,
        'lang': lang
    }
    return Response(context)

@api_view(['GET'])
def course(request):
    id = request.GET.get('course', None)
    lang = request.GET.get('lang', 'ru')
    if id:
        course = get_object_or_404(Course, id=int(id))
        serializer = CourseSerializer(course)
        return Response(serializer.data, status=status.HTTP_200_OK)
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    context = {
        'data': serializer.data,
        'lang': lang
    }
    return Response(context)

@api_view(['GET'])
def team(request):
    id = request.GET.get('id', None)
    lang = request.GET.get('lang', 'ru')
    if id:
        person = get_object_or_404(Team, id=int(id))
        serializer = TeamSerializer(person)
        context = {
            'data': serializer.data,
            'lang': lang
        }
        return Response(context, status=status.HTTP_200_OK)
    team = Team.objects.all()
    serializer = TeamSerializer(team, many=True)
    context = {
        'data': serializer.data,
        'lang': lang
    }
    return Response(context)

@api_view(['GET'])
def vacancy(request):
    id = request.GET.get('id', None)
    lang = request.GET.get('lang', 'ru')
    if id:
        vacancy = get_object_or_404(Vacancy, id=int(id))
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data, status=status.HTTP_200_OK)
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many=True)
    context = {
        'data': serializer.data,
        'lang': lang
    }
    return Response(context)
    
