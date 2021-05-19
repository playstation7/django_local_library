from django.shortcuts import redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    """Регистрирует нового пользователя"""
    if request.method != 'POST':
        # Создание формы решистрации
        form = UserCreationForm()
    else:
        # Обработка заполненой формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Сохранение данных формы в переменную new_user
            new_user = form.save()
            # Создание сеанса с только что зарегестрированным пользователем
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, authenticated_user)
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)
