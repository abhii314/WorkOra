# home/templatetags/custom_filters.py
from django import template
from django.utils.timezone import now

register = template.Library()

@register.filter
def posted_display(posted_date):
    if not posted_date:
        return ''
    
    diff = now() - posted_date

    if diff.days < 1:
        return "Posted today"
    elif diff.days < 7:
        return f"Posted {diff.days} days ago"
    else:
        return posted_date.strftime("Posted on %b %d, %Y")


@register.filter(name='add_class')
def add_class(field, css_class):
    attrs = field.field.widget.attrs
    attrs['class'] = css_class
    attrs['id'] = field.name  # Automatically sets id as field name
    return field
