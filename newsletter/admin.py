from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp, Post

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp"]
	form=SignUpForm
# 	class Meta:
# 		model=SignUp

class PostAdmin(admin.ModelAdmin):
	
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]

	search_fields = ["title", "content"]
	
	class Meta:
		model = Post
		
admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Post, PostAdmin)