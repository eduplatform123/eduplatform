from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

class UserProfile(models.Model):
    USER_TYPES = [
        ('admin', 'Администратор'),
        ('teacher', 'Преподаватель'),
        ('student', 'Студент'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='student')
    student_id = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_user_type_display()}"
    
    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

class FeedbackForm(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает рассмотрения'),
        ('in_progress', 'В работе'),
        ('completed', 'Завершено'),
        ('rejected', 'Отклонено'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_feedback')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_feedback')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher_response = models.TextField(blank=True, null=True, verbose_name='Ответ преподавателя')
    response_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Обратная связь от {self.student.get_full_name()} к {self.teacher.get_full_name()}"
    
    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"
        ordering = ['-created_at']

class FeedbackAttachment(models.Model):
    feedback = models.ForeignKey(FeedbackForm, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='feedback_attachments/', verbose_name='Файл')
    filename = models.CharField(max_length=255, verbose_name='Имя файла')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Вложение: {self.filename}"
    
    def get_filename(self):
        return os.path.basename(self.file.name)
    
    class Meta:
        verbose_name = "Вложение к обратной связи"
        verbose_name_plural = "Вложения к обратной связи"

class UniversityInfo(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержание')
    page_type = models.CharField(max_length=50, verbose_name='Тип страницы')
    is_active = models.BooleanField(default=True, verbose_name='Активна')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Информация об университете"
        verbose_name_plural = "Информация об университете"

class PublicFeedback(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новое'),
        ('in_progress', 'В обработке'),
        ('completed', 'Завершено'),
        ('rejected', 'Отклонено'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Имя')
    theme = models.CharField(max_length=200, verbose_name='Тема')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Сообщение')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def __str__(self):
        return f"Обратная связь от {self.name} - {self.theme}"
    
    class Meta:
        verbose_name = "Публичная обратная связь"
        verbose_name_plural = "Публичная обратная связь"
        ordering = ['-created_at']


class NewsArticle(models.Model):
    """Модель для новостей и блога"""
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('published', 'Опубликовано'),
        ('archived', 'Архив'),
    ]
    
    CATEGORY_CHOICES = [
        ('news', 'Новости'),
        ('blog', 'Блог'),
        ('announcement', 'Объявления'),
        ('event', 'События'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-адрес')
    content = models.TextField(verbose_name='Содержание')
    excerpt = models.TextField(max_length=500, blank=True, verbose_name='Краткое описание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='news', verbose_name='Категория')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    featured_image = models.ImageField(upload_to='news_images/', blank=True, null=True, verbose_name='Изображение')
    tags = models.CharField(max_length=200, blank=True, verbose_name='Теги (через запятую)')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
    is_featured = models.BooleanField(default=False, verbose_name='Рекомендуемая статья')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    published_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)
    
    def get_tags_list(self):
        """Возвращает список тегов"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []
    
    class Meta:
        verbose_name = "Новость/Статья"
        verbose_name_plural = "Новости/Статьи"
        ordering = ['-published_at', '-created_at']
