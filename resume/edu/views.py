from django.shortcuts import render

# Create your views here.
def skill(request):
    s = {'s': "active"}
    return render(request,'edu/skill.html',s)