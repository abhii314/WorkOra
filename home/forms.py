from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'category', 'description', 'salary_min', 'salary_max', 'experience','skill_required', 'salaryPeriod', 'detail_additional']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'skill_required': forms.Textarea(attrs={'rows': 2}),
            'detail_additional': forms.Textarea(attrs={'rows': 4}),

        }
