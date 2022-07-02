from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .tasks import *

def send_mail_without_celery():
    send_mail('CeLerY worked', ' message body ',
              'sumit.jerry1409@gmail.com',
              ['sumit.jerry1409@gmail.com'],
              fail_silently=False
              )
    return None


