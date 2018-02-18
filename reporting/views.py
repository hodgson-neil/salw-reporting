from django.shortcuts import render
from django.utils import timezone

# Create your views here.
from .models import Report


def reports_list(request):
    reports = Report.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'reporting/reports.html', {'reports': reports})