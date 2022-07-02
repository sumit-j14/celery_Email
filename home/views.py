from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .tasks import *

from .helper import *


# with celery page instantly loads and displays to the user
def index(request):
    send_mail_task.delay()
    return HttpResponse("task done")


# wiithout celery LOADED FOR ABOUT 3 SECONDS
# def index(request):
#     send_mail_without_celery()
#     return HttpResponse("task done")
