from django.shortcuts import render
from .models import CybersecurityEvent

def event_list(request):
    events = CybersecurityEvent.objects.all()
    return render(request, 'cybertron/event_list.html', {'events': events})
