from django import forms
from .models import News, Category

# Для не связаных с моделью форм
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Заголовок', widget=forms.TextInput(attrs={"class": "form-control"}))
#     content = forms.CharField(label='Контент новости', required=False, widget=forms.Textarea(attrs={
#         "class": "form-control",
#         "rows": 5
#     }))
#     is_published = forms.BooleanField(label='Опубликовано', initial=True, required=False)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию', widget=forms.Select(attrs={
#         "class": "form-control"
#     }))


# Для связаных с моделью форм
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }
