from django.urls import path
from .import views
from django.contrib.auth import views as auth_views



   
   

urlpatterns = [
    path('', views.home, name='home'),
    # path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('career', views.career, name='career'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page,  name='logout'),
    path('signup', views.signup, name='signup'),
    path('applyJob', views.applyJob, name='applyJob'),
    path('postJob', views.post_job, name='postJob'),
    path('submit/', views.submit_application, name='submit'),

    path('post_job/', views.post_job, name='post_job'),


    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),
    
]
