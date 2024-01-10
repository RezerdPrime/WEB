# from django.http import HttpResponse
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .forms import UserForm
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# import os


from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm
from articles.models import Kostyl, Math_shit, Gender_shit, Yours_planet, Subb
import os

def index(request):
    #return HttpResponse('<h1 style="color:blue">Meine Leben ist vorbei</h1>')
    #os.startfile("https://www.google.ru/")
    return render(request, 'index.html')

def ToPD(request):
    return render(request, 'ToPD.html')

def user_login(request):
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        reg_form = RegisterForm(request.POST)

        if log_form.is_valid():
            cd = log_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            #os.startfile("https://www.google.ru/")
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated successfully')
                    return HttpResponseRedirect('/')


        if reg_form.is_valid():
            #os.startfile("https://www.google.ru/")
            cd = reg_form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                password=cd['password'],
                email=cd['email']
            )

            gendr = cd['gender']
            #os.startfile("https://" + str(user.id))
            koctyl = Kostyl(user_id=user.id,
                            gender_id=gendr)
            koctyl.save()

            plnt = Yours_planet(user_id=user.id,
                                planet=cd['planet'])

            plnt.save()

            math_objs = cd['opros']
            chz = ''
            for mo in math_objs:
                koctyl.Ms.add(Math_shit.objects.get(id=mo))
                chz += ['', 'Gamma function', 'Series of inverse squares', 'Gaussian integral'][int(mo)] + ', '

            login(request, user)
            return render(request, 'reg.html', {'username': cd['username'],
                                                'email': cd['email'],
                                                'planet': cd['planet'],
                                                'gender': ['', 'parquet', 'laminate', 'helicopter boss'][int(cd['gender'])],
                                                'choose': chz[:-2]
                                                })

        if 'HTTP_X_REQUESTED_WITH' in request.META and request.META['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest':
            email = request.POST.get('email')

            if email:  # Проверка наличия email
                subscriber, created = (Subb.objects
                                       .get_or_create(email=email))

                if created: return JsonResponse({'message': 'Thank you for subbing!'})
                else: return JsonResponse({'message': 'You are subbed already'})
            else: return JsonResponse({'message': 'Plz sub'})
        else: return JsonResponse({'message': 'ERROR'})



    else:
        log_form = LoginForm()
        reg_form = RegisterForm()
    return render(request, 'index.html', {'form': log_form, 'reg_form': reg_form})

# def log_user(request):
#     os.startfile("https://www.google.ru/")
#
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#                 user = User.objects.create_user(
#                     username = form.cleaned_data['user_name'],
#                     password = form.cleaned_data['password'],
#                     email = form.cleaned_data['email']
#                 )
#     else:
#         form = UserForm()
#     return render(request, 'user_input.html', {'form': form})

# def log_user(request):
#     os.startfile("https://www.google.ru/")
#
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             #name = form.cleaned_data['name']
#             user = User.objects.create_user(
#                 username = form.cleaned_data['user_name'],
#                 password = form.cleaned_data['password'],
#                 email = form.cleaned_data['email']
#             )
#             login(request, user)
#     else:
#         form = UserForm()
#     return render(request, 'index.html', {'form': form})

    # if request.method == 'post':
    #     os.startfile("https://www.google.ru/")
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['user_name']
    #         password = form.cleaned_data['password']
    #         email = form.cleaned_data['email']
    #         user = authenticate(username=username, password=password, email=email)
    #
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #                 # Пользователь успешно аутентифицирован, выполните необходимые действия
    #                 return redirect("profile")  # Перенаправление на страницу профиля пользователя
    # else:
    #     form = UserForm()
    # return render(request, 'index.html', {'form': form})