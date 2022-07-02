from celery import shared_task
from time import sleep
from django.core.mail import send_mail



# this is task given to celery/redis
# this function basically sleeps the system for duration seconds
@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    send_mail('CeLerY worked', ' message body ',
              'sumit.jerry1409@gmail.com',
              ['sumit.julka149@gmail.com'],
              fail_silently=False
              )
    return None
