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
        widgets = { 'author': forms.TextInput(),
            'subtitle': forms.Textarea(attrs={'class': 'form-control'})
        }

class BusquedaBlogFormulario(forms.Form):
    title = forms.CharField(max_length=40)