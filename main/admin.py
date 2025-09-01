from django.contrib import admin
from .models import (
    UserProfile,
    FeedbackForm,
    FeedbackAttachment,
    UniversityInfo,
    PublicFeedback,
    NewsArticle,
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "user_type", "student_id", "created_at"]
    list_filter = ["user_type", "created_at"]
    search_fields = [
        "user__username",
        "user__first_name",
        "user__last_name",
        "student_id",
    ]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ["student", "teacher", "subject", "status", "created_at"]
    list_filter = ["status", "created_at", "teacher", "student"]
    search_fields = ["subject", "message", "student__username", "teacher__username"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "created_at"


@admin.register(FeedbackAttachment)
class FeedbackAttachmentAdmin(admin.ModelAdmin):
    list_display = ["feedback", "filename", "uploaded_at"]
    list_filter = ["uploaded_at"]
    search_fields = ["filename", "feedback__subject"]
    readonly_fields = ["uploaded_at"]


@admin.register(UniversityInfo)
class UniversityInfoAdmin(admin.ModelAdmin):
    list_display = ["title", "page_type", "is_active", "created_at"]
    list_filter = ["page_type", "is_active", "created_at"]
    search_fields = ["title", "content"]
    readonly_fields = ["created_at", "updated_at"]


@admin.register(PublicFeedback)
class PublicFeedbackAdmin(admin.ModelAdmin):
    list_display = ["name", "theme", "phone", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["name", "theme", "message", "phone"]
    readonly_fields = ["created_at", "updated_at"]
    date_hierarchy = "created_at"


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "category",
        "author",
        "status",
        "is_featured",
        "views_count",
        "published_at",
    ]
    list_filter = ["status", "category", "is_featured", "created_at", "published_at"]
    search_fields = ["title", "content", "excerpt", "tags"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["views_count", "created_at", "updated_at", "published_at"]
    date_hierarchy = "published_at"
    list_editable = ["status", "is_featured"]

    fieldsets = (
        (
            "Основная информация",
            {"fields": ("title", "slug", "content", "excerpt", "author")},
        ),
        ("Классификация", {"fields": ("category", "status", "is_featured", "tags")}),
        ("Медиа", {"fields": ("featured_image",)}),
        (
            "Статистика",
            {
                "fields": ("views_count", "created_at", "updated_at", "published_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    list_editable = ["status"]

    fieldsets = (
        ("Информация о заявителе", {"fields": ("name", "phone")}),
        ("Содержание обращения", {"fields": ("theme", "message")}),
        (
            "Статус и даты",
            {
                "fields": ("status", "created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )
