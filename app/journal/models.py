from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from geopy import Nominatim
from markdown import markdown


class Journal(models.Model):
	title = models.CharField(max_length=30)
	text = models.TextField()
	image = models.ImageField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	is_draft = models.BooleanField(default=False)
	location = models.CharField(max_length=50, null=True)

	class Meta:
		ordering = ['-modified_at']

	def __str__(self):
		return "%s by %s (%s)" % (self.title, self.writer, self.created_at)

	@property
	def mood(self):
		'''
        The overall mood of the entry.
        :return:
        '''
		pass

	@property
	def preview(self):
		'''
        Show a preview of the entry.
        :return:
        '''
		if len(self.text) < 200:
			return self.text

		return "{}...".format(self.text[:200])

	@property
	def word_count(self):
		'''
        Count the number of words in a post
        :return:
        '''
		count = 0
		for word in self.text.split(' '):
			count += 1

		return count

	@property
	def estimated_read_time(self):
		'''
        Estimated amount of time it will take to read a post
        :return:
        '''

		return round(self.word_count / 275)

	@property
	def set_location(self, coordinates):
		locator = Nominatim()
		self.location = locator.reverse(coordinates).address

	def get_text_as_markdown(self):
		return mark_safe(markdown(self.text, safe_mode='escape'))

	def is_editted(self):
		return self.modified_at > self.created_at
