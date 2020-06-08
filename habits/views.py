from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
 

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='habits_list')
    return render(request, 'habits/home.html')

@login_required
def habits_list(request):
    habits = request.user.habits.all()
    return render(request, 'habits/habits_list.html', {'habits' : habits})

@login_required
def habit_detail(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)
    return render(request, 'habits/habit_detail.html', { 'habit' : habit})
