from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    name = request.GET.get("name", "Recruto")
    message = request.GET.get("message", "Давай дружить")
    text = f"Hello {name}! {message}!"
    return HttpResponse(text)
