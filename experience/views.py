from django.shortcuts import render, get_object_or_404
from experience.models import Experience

def experience_list(request, template = 'experience/detail.html'):
    experiences = Experience.objects.all()
    return render(request, template, {'experiences': experiences,})

def experience_detail(request, slug, template='experience/experience.html'):
    experience = Experience.objects.all()
    experience = get_object_or_404(experience, slug=slug)
    return render(request, template, {'experience': experience,})