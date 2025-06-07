import hashlib
from django import template

register = template.Library()

@register.filter
def name_to_color(name):
    """Generate a pastel color based on the company name"""
    hash_val = int(hashlib.sha256(name.encode('utf-8')).hexdigest(), 16)
    hue = hash_val % 360
    return f"hsl({hue}, 70%, 60%)"


@register.filter
def avatar_bg(name):
    """Return pastel hex color from name."""
    hash_val = int(hashlib.md5(name.encode()).hexdigest(), 16)
    hue = hash_val % 360
    return f"hsl({hue}, 70%, 80%)"

@register.filter
def initials(name):
    parts = name.strip().split()
    if parts:
        return parts[0][0].upper()
    return"NA"

