from django.shortcuts import *

# Create your views here.
def verify(request):
    return render(request,'process/verify.html')
    # return HttpResponse("verify page")


