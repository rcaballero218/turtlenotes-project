from django.shortcuts import render

def about(request):
	
	return render(request, "about.html",{})
	

def notes(request):
	
	return render(request, "notes.html",{})

def upload(request):
	
	return render(request, "upload.html",{})

	