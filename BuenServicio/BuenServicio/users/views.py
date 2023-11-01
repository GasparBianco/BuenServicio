from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

# Create your views here.
def users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'users/users.html', context)

def add_user(request):
    grupos = Group.objects.all()
    context = {'grupos': grupos}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        group_name = request.POST['group']

        user = User.objects.create_user(username=username, password=password)
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        context['messsage'] = 'Usuario creado exitosamente'

    return render(request, 'users/adduser.html', context)


def delete_user(request, username):
    user = User.objects.get(username=username)
    if str(user.groups.first()) != 'Administrador':
        user.delete()
    return redirect('users')