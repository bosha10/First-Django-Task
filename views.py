from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template.context import RequestContext
from django.contrib.auth import authenticate,login
from models import User, Post

def index(request):
    return render_to_response('index.html', {'name':request.GET.get('name'),})

def login_user(request):
    kalam = "Please log in below..."
    if request.GET.get('register') == "1":
        state = 'Mabro0k'
    else:

        state = "plz register !"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        userlog = authenticate(username=username, password=password)
        if userlog is not None:
    
            if userlog.is_active:
                login(request,userlog)
                return HttpResponseRedirect("/posts")
            
        #         # //cookie
        #         # class auth  
        #         # database queries
        #         # template doctumenation
        #         return HttpResponseRedirect("/posts")
    
        else:
            kalam = "The username and password were incorrect."

    return render_to_response('auth.html',{'state':state,'kalam':kalam}, context_instance=RequestContext(request))

def register_user(request):
    state = "plz register !"
    newuser = newpassword =''
    newuser = request.POST.get('newuser')
    newpassword = request.POST.get('newpassword')
    if len(newuser)==  0 or  len(newpassword) == 0 :
        return HttpResponseRedirect("/login")
    else :
        temp = User.objects.filter(name__exact = newuser)

        if temp.count() != 0:

            state = "Username taken ya prince.... "

            return HttpResponseRedirect("/login")
        
        else:
            User.objects.create(name=newuser,password=newpassword)
            return HttpResponseRedirect("/login?register=1")



def posts_user(request):

    if User.userlog.is_authenticated():
        allposts = User.userlog.post_set.all();

        return render_to_response('posts.html',{'allpost':allposts}, context_instance=RequestContext(request))
    


