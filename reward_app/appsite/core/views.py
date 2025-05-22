from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import App
from django.contrib.auth import logout
from django.contrib.auth.models import User

def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            apps = App.objects.all().order_by('-created_at')
            return render(request, 'admin_dashboard.html', {"apps":apps})  
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials or not an admin.'})

    return render(request, 'admin_login.html')


@login_required
def admin_add_app_view(request):
    if request.method == 'POST':
        AppName = request.POST.get('appname')
        AppLink = request.POST.get('applink')
        Category = request.POST.get('Category')
        SubCategory = request.POST.get('SubCategory')
        Points = request.POST.get('Points')
        icon = request.FILES.get('icon')

        App.objects.create(
            app_name=AppName,
            app_link=AppLink,
            category=Category,
            sub_category=SubCategory,
            points=Points,
            icon=icon
        )
        apps = App.objects.all().order_by('-created_at')
        submitted = request.GET.get('submitted') == 'true'
        return render(request, 'admin_dashboard.html', {
            "apps": apps,
            "submitted": submitted
        })

    submitted = request.GET.get('submitted') == 'true'
    return render(request, 'add_app.html', {'submitted': submitted})


@login_required
def admin_dashboard_view(request):
    apps = App.objects.all().order_by('-created_at')
    
    return render(request, 'admin_dashboard.html', {"apps": apps, })

@login_required
def admin_logout_view(request):
    logout(request)
    return redirect('admin_login') 

@login_required
def admin_delete_app_view(request, app_id):
    try:
        app = App.objects.get(id=app_id)
        app.delete()
    except App.DoesNotExist:
        pass
    return redirect('admin_dashboard')

@login_required
def admin_edit_app_view(request, app_id):
    app = App.objects.get(id=app_id)
    
    if request.method == 'POST':
        app.app_name = request.POST.get('appname')
        app.app_link = request.POST.get('applink')
        app.category = request.POST.get('Category')
        app.sub_category = request.POST.get('SubCategory')
        app.points = request.POST.get('Points')
        if request.FILES.get('icon'):
            app.icon = request.FILES.get('icon')
        app.save()
        return redirect('admin_dashboard')

    return render(request, 'edit_app.html', {'app': app})

