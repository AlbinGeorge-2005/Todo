from django.shortcuts import render,redirect
from Todoapp.forms import TodoForm,ResgistrationForm,LoginForm
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Todoapp.models import Todo
from django.contrib import messages
# Create your views here.

    
class UserCreationView(View):

    def get(self,request,*args,**kwargs):
        user_form=ResgistrationForm()

        return render(request,'sign_up.html',{'form':user_form})
    
    def post(self,request,*args,**kwargs):

        form_instance=ResgistrationForm(request.POST)

        if form_instance.is_valid():

            # data= form_instance.cleaned_data # this is done in normal Form
            # User.objects.create(**data)
            form_instance.save()# this is done in Model Form. Model Form automatically cleans the errors in data and creates it.
            messages.success(request,"Creation successful")

            return redirect('login')
        return render(request,'sign_up.html')

    

class UserLoginView(View):

    def get(self,request,*args,**kwargs):

        form_instance=LoginForm()

        return render (request,'log_in.html',{'form':form_instance})
    
    def post (self,request,*args,**kwargs):

        form_instance=LoginForm(request.POST)

        if form_instance.is_valid():
            data=form_instance.cleaned_data # Here normal form is used
            
            uname=data.get('username')
            pwd=data.get('password')

            user_obj=authenticate(request,**data)# authenticate --> to check the given username and password are mathiching or not 
            if user_obj: # If the the username and password are matching it redirects to Todo create page(TodoCreateView)

                login(request,user_obj)

               
                return redirect ('todo-create')
            
            else: # if the username and password does not matches the page will remain same.
                messages.success(request,"Invalid login")
                return render (request,'log_in.html',{'form':form_instance})

"""
# request.POST --> <QueryDict: {'csrfmiddlewaretoken': ['iwgjwAMlcKJsMpUHXCstbcXDsYJm7Jq1L5H2Euq2fjZ66ZjKzBBO4Bd6jeyFt7YT'], 'username': ['qqqq'], 'password': ['qqq']}>
[27/May/2025 14:26:44]

cleaned data --> {'username': 'qqqq', 'password': 'qqq'}
"""


class TodoCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=TodoForm()
       
        return render (request,'todo_create.html',{'form':form_instance})
    

    def post (self,request,*args,**kwargs):

        form_instance=TodoForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.user=request.user# form_instance.instance -->form instance have a model that model is the instance

            form_instance.save()
            return render (request,'todo_create.html',{'form':form_instance})
        
class TodoListView(View):

    def get (self,request,*args,**kwargs):

        data=Todo.objects.filter(user=request.user)# the list will be displayed only for login user's todo
        return render (request,'todo_list.html',{'data':data})
    
class TodoDetailView(View):

    def get (self,request,*args,**kwargs):

        id=kwargs.get("pk")
        todo_obj=Todo.objects.get(id=id,user=request.user)# only the particular user can see their detail of their own list

        return render (request,'tododetail.html',{'data':todo_obj})
    
class TodoRemoveView(View):
    def get (self,request,*args,**kwargs):

        id=kwargs.get("pk")
        Todo.objects.get(id=id,user=request.user).delete()
        return redirect ('todo-list')
    
class TodoEditView(View):
    def get (self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todo_obj=Todo.objects.get(id=id,user=request.user)

        form_instance=TodoForm(instance=todo_obj)

        return render(request,'todoupdate.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        todo_obj=Todo.objects.get(id=id,user=request.user)

        form_instance=TodoForm(request.POST,instance=todo_obj)

        if form_instance.is_valid():

            form_instance.save()

            return redirect ('todo-list')
        
        return render(request,'todoupdate.html',{'form':form_instance})
    
class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect('login')








class BaseView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'base.html')
        





        



    


