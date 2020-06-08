from django import forms
from .models import Habit, DailyRecord

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('goal', 'goal_quantity','unit_of_measure')

class RecordForm(forms.ModelForm):
    class Meta:
        model = DailyRecord
        fields = ('quantity', 'unit_of_measure')