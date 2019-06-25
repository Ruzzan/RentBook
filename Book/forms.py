from django import forms
from .models import Book, Comment
class UploadBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'category', 'status', 'image','info','phone','location']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Book Name'}),
            'author':forms.TextInput(attrs={'class':'form-control','placeholder':'Author'}),
            'category':forms.TextInput(attrs={'class':'form-control','placeholder':'Category of Book.'}),
            'info':forms.Textarea(attrs={'class':'form-control','placeholder':'Short Information of Book'}),
            'phone':forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Phone Number'}),
            'location':forms.TextInput(attrs={'class':'form-control','placeholder':'Location with District'}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(label = '',widget = forms.Textarea(attrs={
         'class':'form-control p-0 m-0',
         'id':'content',
         'placeholder':'Your comment here',
         'cols':'50',
         'rows':'3'
     }))

    class Meta:
        model = Comment
        fields = ['content']