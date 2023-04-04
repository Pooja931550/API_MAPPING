from django.shortcuts import render,redirect
from .forms import info
from . forms1 import Project_Detail

#####################################

from . models import User, Student
from .forms import NewUserForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import StudentForm



#######################################

# from . forms import User_Registration
# from . models import Project
#######################################
# from . forms import Person, MembershipForm
# from . forms import Membership
# from . forms import PersonForm
# from django.http import HttpResponse
# from django.contrib import messages




# Create your views here.

# def User(request):
#     if request.method == "Post":
#         Name = request.POST.get("name")
#         email = request.POST.get("email")
#         pho_no = request.POST.get("pho_no")

#         User.objects.create(
#             Name = Name,
#             email = email,
#             pho_no = pho_no,

        # )


        # return render(
        #     request,
        #     "User.html",
        #     {
        #         "msg":"User has been created sccecesfully!!"
        #     }
    #     # )
    # else:
    #     return render(
    #         request,
    #         "User.html"
    #     )

# def UserDetail(request):
#     if request.method == 'POST':
#         fm =User_Registration(request.POST)
#         if fm.is_valid():
#             fm.save()
#             return redirect('/info')

#     else:
#         fm = User_Registration()
#     data = User.objects.all()
#     return render(request, 'User.html', {'form1': fm, 'deta': data})

# def ProjectDetail(request):
#     if request.method == 'POST':
#         fm1 = Project_Detail(request.POST)
#         if fm1.is_valid():
#             fm1.save()
            

#     else:
#         fm1 = Project_Detail()
#     data = Project.objects.all()
#     return render(request, 'Project.html', {'form1': fm1, 'data': data})




# def home(request):
# 	if 'user' in request.session:
# 		current_user = request.session['user']
# 		param = {'current_user': current_user}
# 		return render(request, 'base.html', param)
# 	else:
# 		return redirect('login')
# 	return render(request, 'login.html')




################ ONE TO MANY RELESTIONSHIP THOUGH BY FROM USING THE SESSION ###################


def register_request(request):
    print("inside registration")
    if request.method == "POST":        
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request)
            messages.success(request, "Registration successful." )
            return render (request=request, template_name="login.html", context={})
        else:
            print('user')
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"form":form})


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        # print(uname, pwd)
        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        check_user = User.objects.filter(username=uname, password=pwd)
        print(check_user.query)
        print(check_user)
        if check_user:


            request.session['user'] = check_user[0].id
            form = StudentForm()
            return render(request, 'userhome.html', context={"form":form})
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')
   
def logout(request):
    try:
        request.session.flush()
    except Exception as e:
        print(e)
        return redirect('home')
    return redirect('login')


def getsession(request):
    user =request.session.get('user')
    return render(request, 'app1/getsession.html',{'key':user})



def student_form(request):
    print("inside registration")
    if request.method == "POST":        
        form = StudentForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request)
            messages.success(request, "Registration successful." )
            return render (request=request, template_name="login.html", context={})
        else:
            print('user')
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = StudentForm()
    return render (request=request, template_name="userhome.html", context={"form":form})



def Show(request):
    id = request.session.get('user')
    print(id)
    user = Student.objects.filter(user_id=id)
    return render(request, 'show.html',{'data':user})


def std_form(request):
    # print("inside registration")
    if request.method == "POST":        
        form = StudentForm(request.POST)
        user_id = request.session.get("user")
        print("user: ", user_id)

        if form.is_valid():
            form = form.save(commit=False)
            print(user_id)
            form.user = User.objects.get(id=user_id)
            form.save()
    else:
            print(form.errors)
            print("form is invalid")
            messages.error(request, "Unsuccessful registration. Invalid information.")

    form = StudentForm()
    return render (request=request, template_name="userhome.html", context={"form":form})


###########################################################################################








# def login(request):
#     if request.method == 'POST':
#         personname = request.POST.get('person')
#         pwd = request.POST.get('pwd')
#         check_person = Person.objects.filter(personname=personname, pwd=pwd)
#         if check_person:
#             request.session['person'] = check_person[0].id
#             form = MembershipForm()
#             return render(request, 'userhome.html', context={"form":form})
#         else:
#             return HttpResponse('Please enter valid Personrname or Password.')

#     return render(request, 'login.html')


# def logout(request):
#     try:
#         request.session.flush()
#     except Exception as e:
#         print(e)
#         return redirect('home')
#     return redirect('login')



# def register_request(request):
#     print("inside registration")
#     if request.method == "POST":        
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             Person = form.save()
#             messages.success(request, "Registration successful." )
#             return render (request=request, template_name="login.html", context={})
#         else:
#             messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = PersonForm()
#     return render (request=request, template_name="register.html", context={"form":form})


# def signup(request):
#     if request.method == 'POST':
#         personname = request.POST.get('personname')
#         pwd = request.POST.get('pwd')
#         # print(uname, pwd)
#         if Person.objects.filter(personname=personname).count()>0:
#             return HttpResponse('Username already exists.')
#         else:
#             person = Person(personname=personname, password=pwd)
#             person.save()
#             return redirect('login')
#     else:
#         return render(request, 'signup.html')

# def Show(request):
#     id = request.session.get('person')
#     person = Membership.objects.filter(person_id=id)
#     return render(request, 'show.html',{'data':person})

# def std_form(request):
#     if request.method == "POST":        
#         form = PersonForm(request.POST)
#         person_id = request.session.get("person")
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.person = Person.objects.get(id=person_id)
#             form.save()
#     else:
#             messages.error(request, "Unsuccessful registration. Invalid information.")
#     form = PersonForm()
#     return render (request=request, template_name="userhome.html", context={"form":form})
















