from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import (
    FeedbackForm,
    FeedbackAttachment,
    UserProfile,
    PublicFeedback,
    NewsArticle,
)


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})

        self.fields["username"].label = "Имя пользователя"
        self.fields["password"].label = "Пароль"


class UserRegistrationForm(UserCreationForm):
    student_id = forms.CharField(
        max_length=20, required=True, label="Номер студенческого"
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Имя пользователя"
        self.fields["email"].label = "Email"
        self.fields["password1"].label = "Пароль"
        self.fields["password2"].label = "Подтверждение пароля"

        for field_name, field in self.fields.items():
            if field_name != "student_id":
                field.widget.attrs.update({"class": "form-control"})

        self.fields["student_id"].widget.attrs.update({"class": "form-control"})

    def clean(self):
        cleaned_data = super().clean()
        student_id = cleaned_data.get("student_id")

        if not student_id:
            raise forms.ValidationError("Номер студенческого билета обязателен")

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data


class FeedbackFormForm(forms.ModelForm):
    attachments = forms.FileField(
        widget=forms.FileInput(), required=False, label="Прикрепить файлы"
    )

    class Meta:
        model = FeedbackForm
        fields = ["teacher", "subject", "message"]
        widgets = {
            "teacher": forms.Select(attrs={"class": "form-control"}),
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
        }
        labels = {
            "teacher": "Преподаватель",
            "subject": "Тема",
            "message": "Сообщение",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["teacher"].queryset = User.objects.filter(
                profile__user_type="teacher"
            )


class TeacherResponseForm(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ["status", "teacher_response"]
        widgets = {
            "status": forms.Select(attrs={"class": "form-control"}),
            "teacher_response": forms.Textarea(
                attrs={"class": "form-control", "rows": 5}
            ),
        }
        labels = {
            "status": "Статус",
            "teacher_response": "Ответ преподавателя",
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["student_id"]
        widgets = {
            "student_id": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {
            "student_id": "Номер студенческого",
        }


class PublicFeedbackForm(forms.ModelForm):
    class Meta:
        model = PublicFeedback
        fields = ["name", "theme", "phone", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите ваше имя"}
            ),
            "theme": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите тему обращения"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "+7 (999) 123-45-67"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Опишите ваш вопрос или предложение",
                }
            ),
        }
        labels = {
            "name": "Имя",
            "theme": "Тема",
            "phone": "Номер телефона",
            "message": "Сообщение",
        }


class NewsArticleForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = [
            "title",
            "slug",
            "content",
            "excerpt",
            "category",
            "status",
            "featured_image",
            "tags",
            "is_featured",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Заголовок статьи"}
            ),
            "slug": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "url-adres-stati"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "Содержание статьи...",
                }
            ),
            "excerpt": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Краткое описание статьи (необязательно)",
                }
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
            "featured_image": forms.FileInput(attrs={"class": "form-control"}),
            "tags": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "тег1, тег2, тег3"}
            ),
            "is_featured": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "Заголовок",
            "slug": "URL-адрес",
            "content": "Содержание",
            "excerpt": "Краткое описание",
            "category": "Категория",
            "status": "Статус",
            "featured_image": "Изображение",
            "tags": "Теги",
            "is_featured": "Рекомендуемая статья",
        }
