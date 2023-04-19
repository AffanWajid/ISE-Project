from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home.html')


def announcements(request):
    data = {
        'page': 'Announcements'
    }
    return render(request, 'base.html', data)


def resources(request):
    data = {
        'page': 'Resources'
    }
    return render(request, 'base.html', data)


def attendance(request):
    data = {
        'page': 'Attendance'
    }
    return render(request, 'base.html', data)


def grades(request):
    data = {
        'page': 'Grades'
    }
    return render(request, 'base.html', data)


def assignments(request):
    data = {
        'page': 'Assignments'
    }
    return render(request, 'base.html', data)


def profile(request):
    data = {
        'page': 'Profile'
    }
    return render(request, 'base.html', data)
