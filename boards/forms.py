from django import forms
from .models import Topic , Post , Board

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'What is in your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.',
    )
    class Meta:
        model = Topic
        fields = ['subject', 'message']  # aqui se refere ao campo subject no Model.Topic

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', ]