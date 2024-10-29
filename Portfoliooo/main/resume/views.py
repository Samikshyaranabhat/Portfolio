from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
def about(request):
    return render(request, "about.html")
def projects(request):
   projects_show=[
{"title":"Samikshya connect",
 "path":"css/images/samikshya.jpg"
 },
 {
     "title":"Samikshya connect",
 "path":"css/images/samikshya.jpg"
 },
]

   return render(request, "projects.html",{"projects_show": projects_show})