from django.shortcuts import render, redirect
from .models import Course
# Create your views here.
def index(request):
    context = {
        'all_courses': Course.objects.all(),
    }
    return render(request,"course_app/index.html", context)
def create(request):
    Course.objects.create(name=request.POST['name'],description=request.POST['description'] )

    return redirect('/')
def delete_page(request,id):
    current_course = Course.objects.get(id=id)
    print current_course
    if request.method == "GET":
        return render(request,"course_app/delete_page.html",{"Del_Course" : current_course})

    current_course = Course.objects.get(id=id).delete()
    return redirect('/')
