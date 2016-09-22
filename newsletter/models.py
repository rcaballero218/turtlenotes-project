from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	email=models.EmailField()
	full_name=models.CharField(max_length=120, blank=True,null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	
	def __unicode__(self):
		return self.email


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

	# For python 3
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]
