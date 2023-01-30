from django.shortcuts import render,HttpResponseRedirect
from .forms import Studentform,Searchstudentform
from .models import Student

# Create your views here.



def show(request):
    return render(request,'home.html')


def search(request):
    search_student = request.POST.get('textfield', None)

    if search_student.is_valid():

        query=Student.objects.filter(s_name=search_student)

        context={
            # "title":title,
            "query":query
               
        }





        return render(request,'registered.html')

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
        
        if form.is_valid():
            

            name=form.cleaned_data['s_name'],
            sem=form.cleaned_data['s_current_sem'],
            address=form.cleaned_data['s_address'],
            branch=form.cleaned_data['s_branch'],
            email=form.cleaned_data['s_email'],

            p =Student(s_name=name,s_current_sem=sem,s_address=address,s_branch=branch,s_email=email)
            p.save()
            title="Student Registered Successfully!"
            
            return render(request, 'session.html',{"title":title})



        context={
                "title":title,
                "form":form,
            }



            


            # return render(request, 'register.html',context)

    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = Studentform()

        return render(request, 'register.html',context)