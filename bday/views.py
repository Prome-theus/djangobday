from django.shortcuts import render
from bday.model import bday

def Homepage(request):
    data = {}
    try:
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            msg = request.POST.get('msg')
            song = request.POST.get('song')
            mn = bday(fname = fname,
                      lname = lname,
                      msg = msg,
                      song = song)
            mn.save()
    except:
        pass
        
    return render(request,"index.html")

def main(request):
    return render(request,"home.html")
