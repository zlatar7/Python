from email.policy import default
from django import forms
from AppCoder.models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogFormulario(forms.Form):
   class Meta:
        model = Blog
        fields = "__all__"


class CreateBlogForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        exclude = ('post_date', 'slug')
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'mini_description': forms.Textarea(attrs={'class': 'form-control'})
        }
    
""" class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = "__all__"
        
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
            'blog': forms.TextInput(attrs={'value': '', 'id':'blog', 'type':'hidden'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        } """

class BusquedaBlogFormulario(forms.Form):
    numero = forms.IntegerField()