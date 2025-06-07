from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Job
from .forms import JobForm 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    jobs = Job.objects.all().order_by('-posted_at')
    return render(request, 'index.html', {'jobs':jobs})
    

    
def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def career(request):
    return render(request, 'career.html')

def login_page(request):

    if request.method== "POST":
         username= request.POST.get('username')
         password= request.POST.get('password')

         if not User.objects.filter(username= username).exists():
             messages.error(request, 'Invalid Username')
             return redirect('login_page')
         
         user = authenticate(username = username, password= password)

         if user is None:
             messages.error(request, 'Invalid Password')
             return redirect('login_page')
         else:
             login(request, user)
             return redirect('home')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login')
  

def signup(request):
    # fetch input data from user form

    if request.method=="POST":
        first_name= request.POST.get('first_name')
        last_name= request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')
        confirm_password= request.POST.get('confirm_password')
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

#  check if username is already taken: 
        user = User.objects.filter(username= username)
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('signup')

    # use built-in User object to save data
        user= User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created Successfully')
        
        return redirect('home')
    
    return render(request, 'signup.html')

@login_required(login_url='login')
def applyJob(request):
    return render(request, 'applyJob.html')


@login_required(login_url='login')
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            messages.success(request, "Job Post Created Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = JobForm()
    return render(request, 'jobform.html', {'form': form})

@login_required(login_url='login')
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    job.delete()
    messages.info(request, "Job Deleted!")
    return redirect('home') 

def submit_application(request):
    if request.method=="POST":
        form_type= request.POST.get('form_type')


        if form_type== 'post_job':
               messages.success(request, "Your Job Has Been Posted!")

        elif form_type== 'apply_job':
            messages.success(request, "Thank you! Your application has been submitted successfully.!") 
            # messages.success(request, "Your Job Application Has Submitted!") 
    
        elif form_type== 'contact':
            name = request.POST.get('name', '').strip()
            email = request.POST.get('email', '').strip()
            message = request.POST.get('message', '').strip()
            if name and email and message:
                messages.success(request, "Thank you for contacting!")
                return redirect('home')
            else:
                 messages.error(request, "Please fill in all required fields.")
            return redirect('contact')
        
        else:
            messages.error(request, "Unknown form submission")
            return redirect('home')
        

        return redirect('home')


# Create your views here.
