from .models import *
from django.forms import ModelForm, TextInput, Textarea, FileInput, EmailInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "image","email"]
        widgets = {
            "title": TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Введите заголовок'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            }),

            "image": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Загрузите фото'}),
        }

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        exclude = [""]

