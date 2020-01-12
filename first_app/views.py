from django.http import JsonResponse
from django.shortcuts import render
from first_app.models import Job, Tag
# Create your views here.


def IndexHTML(request):
    filter = []
    for i in request.GET:
        filter.append(i)
    tags = Tag.objects.filter(name__in=filter)
    jobs = Job.objects.filter(tags__in=tags)
    return render(request, 'first_app/base.html', {"jobs": jobs})


def select_jobs_for_tags(request):
    filter = []
    for i in request.POST:
        filter.append(i)
    tags = Tag.objects.filter(name__in=filter)
    jobs = Job.objects.filter(tags__in=tags)
    return JsonResponse(jobs)
#