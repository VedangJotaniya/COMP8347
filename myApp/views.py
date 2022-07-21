from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Course, Student, Order
from django.shortcuts import get_object_or_404
from .forms import *

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

def courses(request):
    course_list = Course.objects.all().order_by('id')
    return render(request, 'myApp/courses.html', {'course_list': course_list})

def place_order(request):
    msg = ''
    courlist = Course.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            if order.course.price > 150:
                order.course.discount()

            if order.levels <= order.course.stages:
                order.save()
                msg = 'Your course has been ordered successfully. '
            else:
                msg = 'You exceeded the number of levels for this course.'
            return render(request, 'myapp/order_response.html', {'msg': msg})
    else:
        form = OrderForm()
    return render(request, 'myapp/placeorder.html', {'form': form, 'msg': msg, 'courlist': courlist})


def coursedetail(request, cour_id):
    course = Course.objects.get(id=cour_id)
    if request.method == 'POST':
        form = InterestForm(request.POST)

        if form.is_valid() and int(form.cleaned_data['interested']) == 1:
            course.interested = course.interested + 1
            course.save()
            msg = "Order was successful"
            return render(request, 'myapp/order_response.html', {'msg': msg})
        else:
            msg = "Some error occured in passing the form"
            return render(request, 'myApp/order_response.html', {'msg': msg})
    else:
        form = InterestForm()
    return render(request, 'myapp/coursedetail.html', {'form': form, 'course': course})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myApp:index'))
            else:
                print('user is not active')
                return HttpResponse('Your account is disabled.')
        else:
            print('username is not valid')
            return HttpResponse('Invalid login details.')
    else:
        return render(request, 'myapp/login.html', {'LoginForm': LoginForm})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myApp:index'))

@login_required
def myaccount(request):
    user = request.user
    msg = ""
    if user.is_staff:
        msg = "You are not a Registered student"
        return render(request, 'myapp/myaccount.html', {'msg': msg})
    else:
        order_list = Order.objects.filter(student__id=user.id)
        interested_topic = Student.objects.filter(username=user.username).values('interested_in__name')
        return render(request, 'myapp/myaccount.html',
                      {'msg': msg, 'firstname': user.first_name, 'lastname': user.last_name, 'orderlist': order_list,
                       'interestList': interested_topic})


