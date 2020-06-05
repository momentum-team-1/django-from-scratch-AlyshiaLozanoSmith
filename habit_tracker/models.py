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