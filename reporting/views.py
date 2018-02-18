from django.shortcuts import render

# Create your views here.


def reports_list(request):
    return render(request, 'reporting/reports.html', {})