from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    # response = HttpResponse()
    # heading1 = '<p>' + 'List of topics: ' + '</p>'
    # response.write(heading1)
    # for topic in top_list:
    #     para = '<p>' + str(topic.id) + ': ' + str(topic) + '</p>'
    #     response.write(para)
    # # Adding courses
    # top_courses = Course.objects.all().order_by('-price')[:5]
    # heading2 = '<p>' + 'List of Courses: ' + '</p>'
    # response.write(heading2)
    # for topic in top_courses:
    #     if topic.for_everyone:
    #         class_choice = "This course is for everyone"
    #     else:
    #         class_choice = "This course is not for everyone"
    #     para = '<p>' + str(topic.id) + ': ' + str(topic) + ' ' + str(class_choice) + '</p>'
    #     response.write(para)

    return render(request, 'myApp/index0.html', {'top_list': top_list})


def about(request):
    # response = HttpResponse()
    # heading1 = '<p> <h1> This is an e-learning website </h1></p>'
    # response.write(heading1)

    return render(request, 'myApp/about0.html')


def detail(request, top_no):
    response = HttpResponse()
    topics = Topic.objects.filter(id=top_no).values()
    if not topics:
        response.write(get_object_or_404(topics))
        return response

    # para = '<p> Category is:  ' + str(topics[0].get('category')) + '</p>'
    # response.write(para)
    courses = Course.objects.filter(topic=top_no)

    # response.write('<ul>')
    # for c in courses:
    #     para = '<li>' + str(c) + '</li>'
    #     response.write(para)
    # response.write('</ul>')

    return render(request, 'myApp/detail0.html', {'topic_name': topics[0].get('category'), 'courses': courses})
