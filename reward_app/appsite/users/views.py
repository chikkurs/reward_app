from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from core.models import App ,Task
from django.db.models import Sum

def user_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username)
        print(password)
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'Username already exists'})
        
        User.objects.create_user(
            username=username, 
            email=email,
            password=password
            )
        return redirect('user_login')
    
    return render(request, 'users/register.html')

def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        # print("test")
        # print(User.objects.all())
      
        # try:
        #     user = User.objects.get(username='Sinta')
        #     user.set_password('123')  
        #     user.save()
        #     u = User.objects.get(username=username)
        #     print("is_staff:", u.is_staff)
        #     print("is_active:", u.is_active)
        #     print("password check:", u.check_password(password))
        # except User.DoesNotExist:
        #     print("User not found for debug")

        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('user_home')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials or not a normal user.'})

    return render(request, 'users/login.html')


    return render(request, 'users/login.html')


@login_required
def user_home_view(request):
    apps = App.objects.all().order_by('-created_at')
    return render(request, 'users/home.html',{"apps":apps} )

@login_required
def user_profile_view(request):

    return render(request, 'users/user_profile_view.html' )

@login_required
def user_point_view(request):
    tasks = Task.objects.filter(user=request.user)
  
    total_points = tasks.aggregate(Sum('points'))['points__sum'] or 0
    print(total_points)

    return render(request, 'users/user_point_view.html', {
        'tasks': tasks,
        'total_points': total_points
    })
 
@login_required
def user_task_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'users/user_task_view.html', {'tasks': tasks})


@login_required
def user_logout_view(request):
    logout(request)
    return redirect('user_login')
def app_detail_view(request, app_id):
    app = App.objects.get(id=app_id)
    if request.method == 'POST':
        screenshot = request.FILES.get('screenshot')
        if screenshot:
            Task.objects.create(
                user=request.user,
                app=app,
                screenshot=screenshot,
                points=app.points  
            )
            return render(request, 'users/app_detail.html', {
                'app': app,
                'message': 'Screenshot uploaded successfully!'
            })
    return render(request, 'users/app_detail.html', {'app': app})


   