from django.db import models
from django.core.urlresolvers import reverse

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Entry(models.Model):
	title =  models.CharField(max_length=200)
	body = models.TextField()
	
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	
	objects = EntryQuerySet.as_manager()

	
	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Bog Entries"
		ordering = ["-created"]
		
def get_absolute_url(self):
    return reverse("entry_detail", kwargs={"slug": self.slug})
 