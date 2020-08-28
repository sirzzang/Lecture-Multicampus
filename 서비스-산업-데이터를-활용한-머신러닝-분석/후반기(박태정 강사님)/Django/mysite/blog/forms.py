from django import forms

class PostSearchForm(forms.Form): # forms에서 Form 클래스 상속받음.
    search_word = forms.CharField(label='Search Word')