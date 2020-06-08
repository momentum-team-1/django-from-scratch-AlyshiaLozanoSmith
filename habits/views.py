from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import HabitForm, RecordForm
 

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

@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect(to='habit_detail', habit_pk=habit.pk)
    else:
        form = HabitForm()    
    
    return render(request, 'habits/add_habit.html', {'form':form})

@login_required
def add_record(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.habit = habit
            record.save()
            return redirect(to='habit_detail', habit_pk=habit.pk)
    else:
        form = RecordForm()
    return render(request, 'habits/add_record.html', {'form': form, 'habit':habit} )

@login_required
def edit_habit(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == 'POST':
        form = HabitForm(instance=habit, data=request.POST)
        if form.is_valid():
            habit = form.save()
            return redirect(to='habit_detail', habit_pk=habit.pk)
    else:
        form = HabitForm(instance=habit)
    
    return render(request, 'habits/edit_habit.html', {'form': form, 'habit':habit} )

@login_required
def delete_habit(request, habit_pk):
    habit = get_object_or_404(request.user.habits, pk=habit_pk)

    if request.method == 'POST':
        habit.delete()
        return redirect(to='habits_list')
    
    return render(request, "habits/delete_habit.html", { "habit": habit })

        
