from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, "index.html")


def team(request):
    return render(request, "team.html")
