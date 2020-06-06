from django.shortcuts import render, redirect

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='habits_list')
    return render(request, 'habits/home.html')

def habits_list(request):
    habits = request.user.habits.all()
    return render(request, 'habits/habits_list.html', {'habits' : habits})