from django.db import models
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='habit')
    name = models.CharField(max_length = 500) 
    goal_quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class DailyRecord(models.Model):
    habit = models.ForeignKey(to=Habit,
                              on_delete = models.CASCADE,
                              related_name='dailyrecord')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    recorded_on = models.DateField(null=True, blank=True)
    
    class meta:
        unique_together = [['habit','recorded_on']]

    def __str__(self):
        return f"you made progress towards your goal! {self.quantity}{self.recorded_on}"
