from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]

    return render(request, 'myApp/index.html', {'top_list': top_list})


def about(request):

    return render(request, 'myApp/about.html')


def detail(request, top_no):
    response = HttpResponse()
    topics = Topic.objects.filter(id=top_no).values()
    if not topics:
        response.write(get_object_or_404(topics))
        return response

    courses = Course.objects.filter(topic=top_no)

    return render(request, 'myApp/detail.html', {'topic_name': topics[0].get('category'), 'courses': courses})
