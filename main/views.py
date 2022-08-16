from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Отображение главной страницы
def home_page(request):
    return render(request, 'main/home.html', {})


# Отображение страницы со всеми продуктами
def foods_page(request):
    all_foods = models.Foods.objects.all()
    rating = models.Rating.objects.all()
    category = models.Category.objects.all()

    context = {
        'all_foods': all_foods,
        'rating': rating,
        'category': category
    }
    return render(request, 'main/foods.html', context)


def register_page(request):
    '''
    Контроллер, отвечающий за логику:
    - отображения страницы регистрации
    - регистрации пользователя
    '''
    if request.method == "POST":
        # Регистрация пользователя при POST запросе
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

    # Возвратить страницу регистрации при GET запросе
    return render(request, 'main/register.html', {})


def login_page(request):
    '''
        Контроллер, отвечающий за логику:
        - отображения страницы логина
        - аутентификации пользователя
    '''
    if request.method == "GET":
        return render(request, "main/login.html", {})
    #if request.method == "POST":
    else:
        # Аутентификация пользователя при POST запросе
        username = request.POST.get("login", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)

        # Если пользователь существует и данные верны: перенаправить в страницу профиля
        if user:
            login(request, user)
            return redirect(reverse("main:profile_page"))

        # Если данные неверны: возвратить сообщение о некорректных данных
        return render(request, "main/login.html", {"error": "Неправильный логин или пароль"})
    # else:
    # # Возвратить страницу логина при GET запросе
    #     return render(request, "main/login.html", {})


def logout_view(request):
    '''
        Контроллер, отвечающий за логику:
        - выхода из аккаунта
    '''
    logout(request)
    return redirect(reverse('main:home_page'))


def results_page(request):
    '''
        Контроллер, отвечающий за логику:
        - поискового запроса
    '''
    search_pattern = request.GET.get("search", None)

    # Если поисковой запрос не пустой, то найти подходящие продукты
    if search_pattern and len(search_pattern) > 0:
        all_foods = models.Foods.objects.filter(name__icontains=search_pattern[0])
    else:
        # В ином случае вывести все продукты
        all_foods = models.Foods.objects.all()

    context = {
        'all_foods': all_foods,
    }
    return render(request, 'main/foods.html', context)


def food_detail_page(request, pk):
    '''
        Контроллер, отвечающий за логику:
        - отображения страницы продукта
        - возможность заказа клиентами продуктов
    '''
    food = models.Foods.objects.get(pk=pk)
    food_price = food.price

    comments = models.Comment.objects.filter(food=food)

    if request.method == "POST":
        try:
            # Добавление заказа при POST заросе
            f_name = request.POST.get("first_name")
            l_name = request.POST.get("last_name")
            p_number = request.POST.get("phone_number")
            address = request.POST.get("address")
            f_count = request.POST.get("food_count")

            models.Orders.objects.create(
                food=food,
                first_name=f_name,
                last_name=l_name,
                phone_number=p_number,
                address=address,
                food_count=f_count,
                price=food_price * int(f_count)  # Вычисляем цену заказа в зависимости от количества заказанного продукта
            )
            return redirect(reverse('main:food_detail_page', args=(pk,)))
        except Exception as exc:
            print("При создании пользователя произошла ошибка", request.POST, exc)
            error = {
                'error_code': exc,
                'message': 'Проверьте корректность введенных данных'
            }
            return render(request, 'main/food_detail.html', {"error": error, 'food': food, 'comments': comments})

    # возвратить страницу продукта при GET запросе
    return render(request, 'main/food_detail.html', {'food': food, 'comments': comments})


def add_comment_view(request, pk):
    '''
        Контроллер, отвечающий за логику:
        - комментирования продуктов
    '''

    if request.user.is_authenticated:
        # Если пользователь аутентифицирован: использовать его имя пользователя
        author = request.user.username
    else:
        # В ином случае: использовать переданное имя
        author = request.POST.get("author", None)

    food = models.Foods.objects.get(pk=pk)
    comment_text = request.POST.get("comment", None)
    models.Comment.objects.create(
        author=author,
        comment_text=comment_text,
        food=food,
    )
    # перенаправить на страницу продукта
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
    # если пользователь не аутентифицирован: перенаправить на страницу логина
    return redirect(reverse("main:login_page"))


def profile_delete_view(request):
    """
        Контроллер, отвечающий за логику:
        - удаления пользователя
    """

    # Если пользователь аутентифицирован: удалить пользователя
    if request.user.is_authenticated:
        try:
            user = request.user
            user.delete()
            return redirect(reverse('main:home_page'))
        except Exception as exc:
            print(f"при удалении пользователя {request.user.pk} произошла ошибка", exc)

        return redirect(reverse('main:profile_page'))

    # Если пользователь не аутентифицирован: перенаправить на страницу логина
    return redirect(reverse('main:login_page'))


def contact_us_page(request):
    """
        Контроллер, отвечающий за логику:
        - связь пользователя с тех. поддержкой
    """

    # отправка сообщения в тех. поддержку при POST запросе
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        message = request.POST.get("message")
        models.Questions.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            message=message
        )
        return redirect(reverse('main:contact_us_page'))

    # возвратить страницу связи с тех. поддержкой при GET запросе
    return render(request, 'main/contact_us.html', {})


def career_page(request):
    """
        Контроллер, отвечающий за логику:
        - связь пользователя с тех. поддержкой
    """

    # отправка заявки на трудоустройство при POST запросе
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        stuff = request.POST.get("stuff")
        message = request.POST.get("message")
        models.Career.objects.create(
            full_name=full_name,
            email=email,
            stuff=stuff,
            message=message
        )
        return redirect(reverse('main:career_page'))

    # возвратить страницу карьеры при GET запросе
    return render(request, 'main/career.html', {})


# Отображение бизнес страницы
def business_page(request):
    return render(request, 'main/business.html', {})


# Отображение страницы истории
def history_page(request):
    return render(request, 'main/history.html', {})


def add_rate_view(request, pk):
    """
        Контроллер, отвечающий за логику:
        - добавления рейтинга
        - замены рейтинга
        Отображается последний добавленный рейтинг
    """
    food = models.Foods.objects.get(pk=pk)
    star = request.POST.get('rate', None)

    try:
        # если рейтинг уже имеется, то заменить его на текущий
        if models.Rating.objects.get(food=food):
            rate = models.Rating.objects.get(food=food)
            rate.food = food
            rate.star = star

            rate.save()

    except Exception as exc:
        # если не имеется, то создать новый
        try:
            models.Rating.objects.create(
                food=food,
                star=star
            )
        except Exception:
            return redirect(reverse('main:food_detail_page', args=(pk,)))

    return redirect(reverse('main:food_detail_page', args=(pk,)))


def category_view(request, pk):
    food = models.Foods.objects.get(pk=pk)

    # Если поисковой запрос не пустой, то найти подходящие продукты
    all_foods = models.Foods.objects.filter(category=food.category)

    context = {
        'all_foods': all_foods,
    }
    return render(request, 'main/foods.html', context)