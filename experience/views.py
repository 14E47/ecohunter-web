from django.shortcuts import render, get_object_or_404
from experience.models import Experience

def experience_list(request, template = 'experience/detail.html'):
    n = 5
    experiences = Experience.objects.all()
    experience_f = [experiences[i:i + n] for i in range(0, len(experiences), n)]
    return render(request, template, {'experiences': experience_f,})

def experience_detail(request, slug, template='experience/experience.html'):
    experience = Experience.objects.all()
    experience = get_object_or_404(experience, slug=slug)
    return render(request, template, {'experience': experience,})