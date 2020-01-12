from django.shortcuts import render

# Create your views here.


def IndexHTML(request):
    return render(request, 'first_app/base.html')