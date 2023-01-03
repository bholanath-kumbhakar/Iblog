
from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blog.models import Post, Contact_Us
from datetime import datetime
from django.views.generic import ListView

# Create your views here.

#signin
class LoginView(View):

    def get(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')
        else:
            return render(request,'blog/login.html')

    def post(self,request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/dashboard/')
        else:
            un =request.POST.get('username')
            ps=request.POST.get('password')
            user=authenticate(username=un,password=ps)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponseRedirect("/signup/")


#logout view
@method_decorator(login_required,name="dispatch")
class log_out(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/')



class signup(View):
    def get(self,request):
        return render(request,'blog/signup.html')
    def post(self,request):
        un =request.POST.get('username')
        ps=request.POST.get('password')
        fn=request.POST.get('firstname')
        ln=request.POST.get('lastname')
        email=request.POST.get('email')
        user = User.objects.create_user(username=un,password=ps,first_name=fn,last_name=ln,email=email)
        messages.success(request,'account created successfully')
        user.save()
        return HttpResponseRedirect('/dashboard/')

#dashboard view
@method_decorator(login_required, name='dispatch')
class dashboard(View):
    def get(self,request):
        userpost=Post.objects.filter(author=request.user)
        return render(request,'blog/dashboard.html',{'userpost':userpost})
        


#pagination
class homeview(ListView):
    paginate_by=8
    template_name = 'blog/home.html'
    model=Post
    context_object_name='posts'
    def get_queryset(self):
        return Post.objects.all().order_by('published_at').reverse()

class aboutview(View):
    """
    This class used for About us page
    """
    def get(self,request):
        return render(request,'blog/about.html')


class  contactusview(View):
    """
    this is contact us view
    """
    def get(self,request):
        return render(request,'blog/contactus.html')

    def post(self,request):

        name =request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        obj=Contact_Us.objects.create(name=name,email=email,mobile=phone,message=message)
        obj.save()
        messages.success(request,'account created successfully')
        return render(request,'blog/contactus.html')

#postDetailsView
 
class postdetailsview(View):
    def get(self,request,id):
        post=Post.objects.filter(id=id).first()
        allpost=Post.objects.all().exclude(id=id)
        return render(request,'blog/postdetails.html',{'post':post,'allpost':allpost})
        
#addpostview
@method_decorator(login_required, name='dispatch')
class addpostview(View):
    def get(self,request):
        return render(request,'blog/addpost.html')
    def post(self,request):
        title=request.POST.get('title')
        desc=request.POST.get('description')
        image = request.FILES.get('image')
        published_at=datetime.now()
        obj=Post(title=title,description=desc,image=image,author=request.user,published_at=published_at)
        obj.save()
        return HttpResponseRedirect('/dashboard/')

#editview
@method_decorator(login_required, name='dispatch')
class editpost(View):
    def get(self,request,id):
        post=Post.objects.filter(id=id).first()
        return render(request,'blog/editpost.html',{'post':post})
    def post(self,request,id):
        title=request.POST.get('title')
        desc=request.POST.get('description')
        image = request.FILES.get('image')
        post=Post.objects.get(id=id)
        post.title=title
        post.description=desc
        if image:
            post.image=image
        post.save()

        return HttpResponseRedirect('/dashboard/')

#deleteview
@method_decorator(login_required, name='dispatch')
class deleteview(View):
    def get(self,request,id):
        pi=Post.objects.filter(id=id)
        pi.delete()
        return HttpResponseRedirect("/dashboard/")


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request, id):
        user = User.objects.filter(id=id).first()
        return render(request, 'blog/signup.html')

    def post(self, request, id):
        fn=request.POST.get('firstname')
        ln=request.POST.get('lastname')
        email=request.POST.get('email')
        user=User.objects.get(id=id)
        user.first_name=fn
        user.last_name=ln
        user.email=email
        user.save()
        return HttpResponseRedirect ('/dashboard/')


