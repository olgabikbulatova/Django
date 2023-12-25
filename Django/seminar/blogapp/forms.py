import datetime
from django import forms
from .models import Author, Post


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}))
    lastname = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите фамилию автора блаблабла'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    bio = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    bday = (forms.DateField(initial=datetime.date.today,
                            widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})))


class PostForm(forms.ModelForm):
    # def __init__(self, authors_list, *args, **qwargs):
    #     super(PostForm, self).__init__(*args, **qwargs)
    #     self.fields['author'] = forms.ChoiceField(choices=tuple([name,name] for name in authors_list))

    class Meta:
        model = Post
        fields = ('title', 'content', 'author')





