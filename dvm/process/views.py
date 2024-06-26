from django.shortcuts import *
from .models import *
from django.contrib import messages
# Create your views here.
def verify(request):
    if request.method == "POST":
        voter_id = request.POST.get('voter_id')
        user = voter_Details.objects.filter(voter_id=voter_id)
        if user.exists():
            voter = get_object_or_404(voter_Details, voter_id=voter_id)
            if voter.is_voted:
                messages.error(request, 'Already Voted.')
            else:
                opposition_list = oppositions.objects.all()
                return render(request, "process/voting.html" ,{'voter_id': voter_id,'opposition_list': opposition_list})
        else:
            messages.error(request, 'Invalid Voterid')
    return render(request,'process/verify.html')

def vote(request):
    if request.method == "POST":
        # form sends the party_id along with the vote request
        voter_id = request.POST.get('voter_id')
        opposition_id = request.POST.get('opposition_id')
        voter = get_object_or_404(voter_Details, voter_id=voter_id)
        try:
            opposition = get_object_or_404(oppositions, op_id=opposition_id)
            # Mark the voter as voted
            if not voter.is_voted:
                opposition.vote_count += 1
                opposition.save()
                voter.is_voted = True
                voter.save()
                return HttpResponse("voted " + voter_id)
            else:
                messages.error(request, 'Already Voted.')
                return redirect(verify)
        except :
            if not voter.is_voted:
                voter.is_voted = True
                voter.save()
                return HttpResponse("voted " + voter_id)
            else:
                messages.error(request, 'Already Voted.')
                return redirect(verify)



    return redirect('verify')
def index(request):
    return render(request,'home/index.html')


def results(request):
    opposition_list = oppositions.objects.all()
    checkk=voteends.objects.all()
    return render(request,'process/resutls.html',{'opposition_list': opposition_list,'checkk':checkk})
