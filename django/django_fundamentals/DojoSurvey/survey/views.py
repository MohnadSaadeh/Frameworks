from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request, "index.html" )

def theresult(request):

    name_main = request.POST['name']
    location_main = request.POST['location']
    language_main  = request.POST['language']
    messege_main  = request.POST['message']
    
    context = {
        "name": name_main,
        "language": language_main,
        "message": messege_main ,
        "location" : location_main
    }
    return render(request, "result.html",context )
