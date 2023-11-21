from django.shortcuts import *
from .models import *
from django.contrib import messages
# Create your views here.
def verify(request):
    if request.method == "POST":
        voter_id = request.POST.get('voter_id')
        user = voter_Details.objects.filter(voter_id=voter_id)
        if user.exists():
            return render(request, "process/voting.html")
        else:
            messages.error(request, 'Invalid Voterid')
    return render(request,'process/verify.html')


def done(request):
    return render(request, "index1.html")
def index(request):
    return render(request,'home/index.html')



