from django.db import models
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('normal', 'Нормальный'),
        ('urgent', 'Срочный'),
        ('backlog', 'Бэклог'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='normal')
    start_date = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
