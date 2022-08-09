from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def foods_page(request):
    all_foods = models.Foods.objects.all()



    context = {
        'all_foods': all_foods,

    }
    return render(request, 'main/foods.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("login", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse("main:profile_page"))

        return render(request, "main/login.html", {"error": "Неправильный логин или пароль"})
    return render(request, "main/login.html", {})


def home_page(request):
    return render(request, 'main/home.html', {})


def results_page(request):
    search_pattern = request.GET.get("search", None)
    if search_pattern and len(search_pattern) > 0:
        all_foods = models.Foods.objects.filter(name__icontains=search_pattern[0])
    else:
        all_foods = models.Foods.objects.all()

    context = {
        'all_foods': all_foods,
    }

    return render(request, 'main/foods.html', context)


def food_detail_page(request, pk):
    food = models.Foods.objects.get(pk=pk)
    comments = models.Comment.objects.filter(food=food)

    if request.method == "GET":
        return render(request, 'main/food_detail.html', {'food':food, 'comments':comments})
    else:
        author = request.POST.get("author", None)
        comment_text = request.POST.get("comment", None)
        models.Comment.objects.create(
            author=author,
            comment_text=comment_text,
            food=food,
        )
        return redirect(reverse('main:food_detail_page', args=(pk,)))


def profile_page(request):
    """
    Контроллер, отвечающий за логику:
    - отображения профиля пользователя
    - изменения данных пользователя
    Пользователь должен быть аутентифицирован
    """
    if request.user.is_authenticated:
        # изменение данных пользователя при POST запросе
        if request.method == "POST":
            password = request.POST.get("password", None)
            first_name = request.POST.get("first_name", None)
            last_name = request.POST.get("last_name", None)

            user = request.user

            if password:
                user.set_password(password)

            if first_name:
                user.first_name = first_name

            if last_name:
                user.last_name = last_name

            user.save(update_fields=['password', 'first_name', 'last_name'])

            # если было изменение пароля, значит перенаправить на страницу аутентификации
            # так как сессия должна быть пересоздана
            if password:
                return redirect(reverse('main:login_page'))

            return redirect(reverse('main:profile_page'))

        # возвратить страницу профиля при GET запросе
        return render(request, 'main/profile.html', {})
    return redirect(reverse("main:login_page"))


def logout_view(request):
    logout(request)
    return redirect(reverse('main:home_page'))


def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get("login", None)
            password = request.POST.get("password", None)
            email = request.POST.get("email", None)
            first_name = request.POST.get("first_name", None)
            last_name = request.POST.get("last_name", None)
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            return redirect(reverse('main:login_page'))
        except Exception as exc:
            print("При создании пользователя произошла ошибка", request.POST, exc)
            error = {
                'error_code': exc,
                'message': 'Проверьте корректность введенных данных'
            }
            return render(request, 'main/register.html', {"error": error})

    return render(request, 'main/register.html', {})

def profile_delete_view(request):
    if request.user.is_authenticated:
        try:
            user = request.user
            user.delete()
            return redirect(reverse('main:home_page'))
        except Exception as exc:
            print(f"при удалении пользователя {request.user.pk} произошла ошибка", exc)
        return redirect(reverse('main:profile_page'))

    # Если пользователь не аутентифицирован, перенаправить на страницу логина
    return redirect(reverse('main:login_page'))