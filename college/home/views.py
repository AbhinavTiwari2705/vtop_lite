from django.shortcuts import render,HttpResponseRedirect
from .forms import Studentform,Searchstudentform
from .models import Student

# Create your views here.


def show(request):
    return render(request,'home.html')


def search(request):
    print("search")
    search_student = request.GET.get('textfield', None)
    query=Student.objects.filter(s_name=search_student)
    context={
        "query": query            
    }

    return render(request,'registered.html', context)


def registered(request):
    title="All registered Student"
    query=Student.objects.all()
    context={
        "title":title,
        "query":query
    }

    return render(request,'registered.html',context)


def register(request):
    # if this is a POST request we need to process the form data
    title="New Student Registration"
    form = Studentform(request.POST or None)
    context={
        "title":title,
        "form":form,
    }
    if form.is_valid():
        form_cleaned_data = form.cleaned_data
        print(form_cleaned_data)
        student = Student(**form_cleaned_data)
        student.save()
        title="Student Registered Successfully!"
        
    return render(request, 'register.html',context)