from django.shortcuts import render

# Create your views here.
def planning_operation(request):
    return render(request, 'planning_operation/operational.html')