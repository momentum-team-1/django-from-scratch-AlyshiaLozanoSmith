from django.db import models
from django.contrib.auth.models import AbstractUser
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='habits')
    name = models.CharField(max_length = 500) 
    goal_quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit,
                              on_delete = models.CASCADE,
                              related_name='records')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    recorded_on = models.DateField(auto_now=True, null=True, blank=True)
    
    class meta:
        unique_together = ['habit','recorded_on']

    def __str__(self):
        return f"{self.quantity}:{self.recorded_on}"
