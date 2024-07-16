from cars.models import Add_Car
from django import forms 
from cars.models import Comment

class AddCarForms(forms.ModelForm):
    class Meta:
        model = Add_Car
        fields = "__all__"

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']