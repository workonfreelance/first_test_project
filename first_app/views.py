from django.http import JsonResponse
from django.shortcuts import render
from first_app.models import Job, Tag
# Create your views here.


def temp(request):

    return render(request, 'test_temp_len/main.html')

def IndexHTML(request):
    filter = []
    print(request.GET)
    for i in request.GET:
        if i == "filter":
            continue
        filter.append(i)

    if len(filter)>0:
        tags = Tag.objects.filter(name__in=filter)
        jobs = Job.objects.filter(tags__in=tags)
        Job.objects.all()
    else:
        jobs = Job.objects.all()
    return render(request, 'first_app/base.html', {"jobs": jobs})


def select_jobs_for_tags(request):
    filter = []
    for i in request.POST:
        filter.append(i)
    tags = Tag.objects.filter(name__in=filter)
    jobs = Job.objects.filter(tags__in=tags)
    return JsonResponse(jobs)
#