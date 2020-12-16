from aljoadmin.models import Comment
from django import forms

class CommentForm(forms.ModelForm):
	content = forms.CharField(
		widget=forms.Textarea(attrs={'style':'width:100%; height:80px;'}),
		label=''
	)
	class Meta:
		model = Comment
		fields = ('content',)