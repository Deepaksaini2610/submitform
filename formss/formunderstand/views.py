from django.shortcuts import render
from .models import bharti
# Create your views here.
def index(request):

    data = {
        "currentname":'deepak saini'
    }
    sdata = bharti.objects.all()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        meraname = bharti(fname = fname,lname = lname)
        meraname.save()
    return render(request,'index.html')