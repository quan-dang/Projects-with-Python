from django import forms
from .models import Comment
 
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

""" ModelForm is a dynamic form, different from the form is used to build email delivery """
class CommentForm(forms.ModelForm): 
	class Meta:
		model = Comment # indicate which model to use to build the form
		fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
	query = forms.CharField()