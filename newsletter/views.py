from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import  ContactForm, SignUpForm

# Create your views here.

def home(request):
	title = "Welcome"
	form=SignUpForm(request.POST or None)
	context={
		"title":title,
		"form": form
	}
	if request.user.is_authenticated():
		title = "Welcome %s"%(request.user)

	if request.method == "POST":
		print request.POST
		
	if form.is_valid():
		instance=form.save(commit=False)	
		full_name=form.cleaned_data.get("full_name")
		if not full_name:
			full_name="Unknown"
		instance.full_name=full_name
		# or use below for just one instance, not using form
		# if not instance.full_name:
        # 	 instance.full_name ="Unknown"
		instance.save()
		print instance.email
		print instance.timestamp
		context={
			"title":"Sign Up Successful! Thank you"
		}

	return render(request, "home.html",context)

def contact(request):
	form =ContactForm(request.POST or None)
	
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message=form.cleaned_data.get("message")
		form_full_name=form.cleaned_data.get("full_name")
		#print email, message,full_name
		subject='Site contact form'
		from_email=settings.EMAIL_HOST_USER
		to_email=[from_email,'rcaballero218@yahoo.com']
		contact_message="%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)
			
		send_mail(subject,
			contact_message, 
			from_email, 
			to_email, 
			fail_silently=False)
		
	context = {
		"form":form,
	}

	return render(request,"forms.html", context)

