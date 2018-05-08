# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import status


def handle404(request):
    return render(request, 'recipes/404.html', status=status.HTTP_404_NOT_FOUND)


def home(request):
    return render(request, 'recipes/home.html')