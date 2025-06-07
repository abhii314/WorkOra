from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Employer(models.Model):
    User= models.OneToOneField(User, on_delete=models.CASCADE)
    aadhaar_number= models.CharField(max_length=12, unique=True)
    is_verified= models.BooleanField(default=False)
    gst_number= models.CharField(max_length=15, blank=True)



class Job(models.Model):
    CATEGORY_CHOICES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Urgent', 'Urgent'),
        ('Contract', 'Contract')
    ]
    EXP_CHOICES =[
        ('No Experience', 'No Experience'),
        ('0-1 Years', '0-1 Years'),
        ('1-3 Years', '1-3 Years'),
        ('3-5 Years', '3-5 Years'),
        ('5+ years', '5+ years')
    ]
    SALARY_PERIOD =[
        ('Daily', 'Daily'),
        ('Week', 'Week'),
         ('Month', 'Month'),
        ('Year', 'Year'),
       
    ]
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Full-Time')
    location = models.CharField(max_length=100)

    # Salary range (in ₹ or as per your preference)
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    salaryPeriod = models.CharField(max_length=20, choices=SALARY_PERIOD, default='Daily')

    experience = models.CharField(max_length=20, choices=EXP_CHOICES, default='No Experience')
 # e.g. "2+ years", "Fresher"
    
    # General summary
    description = models.TextField()

    # Structured job details
    skill_required = models.TextField(blank=True, null=True)
    detail_additional = models.TextField(blank=True, null=True)

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
   
    


    def __str__(self):
        return f"{self.title} at {self.company}"

    def formatted_salary(self):
        return f"₹{self.salary_min:,} - ₹{self.salary_max:,}"
