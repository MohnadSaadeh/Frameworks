from django.shortcuts import render
from datetime import datetime
# Create your views here.
def timePage(request):

    now = datetime.now()
    context = {
        
        "timeDay": now.strftime("%b %d , %Y"),
        "timeHour": now.strftime("%H:%M %p")

    }
    return render(request , "index.html" ,context )


    