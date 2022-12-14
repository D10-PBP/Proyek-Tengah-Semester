from django.shortcuts import render
from fitur_autentikasi.models import Profile, User
from leaderboard.models import Message
from leaderboard.forms import UploadMessage
from django.shortcuts import render
from django.db.models import Sum
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from random import choice
from django.views.decorators.csrf import csrf_exempt

# Menampilakn leaderboard
@login_required(login_url="/login/")
def leaderboard(request):
    return render(request, 'leaderboard.html')

# Memberikan data user dalam leaderboard dalam bentuk json
def show_json(request):
    num_of_user = Profile.objects.count()
    data = []
    counter = 1

    if num_of_user < 10:
        temp = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')
    else:
        temp = Profile.objects.alias(
        total_points=Sum('poin')
        ).order_by('-total_points')[:10]

    for item in temp:
        if counter == 1:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 1})
            counter += 1
        elif counter == 2:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 2})
            counter += 1
        elif counter == 3:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 3})
            counter += 1
        else:
            data.append({'username' : item.user.username, 'poin' : item.poin, 'status' : 4})
            counter += 1
    return JsonResponse(data, safe=False)

# Menambahkan pesan dari user
def add_message (request):
    form = UploadMessage(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            random_message = request.POST.get("random_message")
            new_message = Message(random_message=random_message)
            new_message.save()
            return HttpResponse(b"CREATED", status=201)
        else :
            form = UploadMessage
    return HttpResponse(b"CREATED", status=201)

# Menampilkan salah satu pesan dari user secara acak
def show_message_json (request):
        pks = Message.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        selected_message = Message.objects.get(pk=random_pk)
        context = {
            "data" : selected_message
        }
        data_message = [{'message' : selected_message.random_message}]
        return JsonResponse(data_message, safe=False)

@csrf_exempt
def add_message_from_flutter (request):
    if request.method == "POST":
        random_message = request.POST.get('message')
        new_message = Message(random_message=random_message)
        new_message.save()
        response = {
            "message" : new_message.random_message
        }
        return JsonResponse(response,status=200)