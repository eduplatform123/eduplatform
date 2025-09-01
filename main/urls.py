from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_university, name='about'),
    path('contact/', views.contact_info, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('advantages/', views.advantages, name='advantages'),
    path('programs/', views.programs, name='programs'),
    path('mission/', views.mission, name='mission'),
    path('feedback/', views.public_feedback, name='public_feedback'),
    
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html', form_class=CustomLoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    
    path('feedback/create/', views.create_feedback, name='create_feedback'),
    path('feedback/form/', views.feedback_form, name='feedback_form'),
    path('feedback/<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
    path('feedback/attachment/<int:attachment_id>/download/', views.download_attachment, name='download_attachment'),
    
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage-users/', views.manage_users, name='manage_users'),
    path('manage-university-info/', views.manage_university_info, name='manage_university_info'),
    path('download-teacher-statistics/', views.download_teacher_statistics, name='download_teacher_statistics'),
    path('mark-public-feedback-worked/<int:feedback_id>/', views.mark_public_feedback_worked, name='mark_public_feedback_worked'),
    path('public-feedback-detail/<int:feedback_id>/', views.public_feedback_detail, name='public_feedback_detail'),
    
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    
    path('dashboard/news/create/', views.create_news_article, name='create_news_article'),
    path('dashboard/news/edit/<int:article_id>/', views.edit_news_article, name='edit_news_article'),
    
    path('dashboard/public-feedback/', views.admin_public_feedback_list, name='admin_public_feedback_list'),
    path('dashboard/internal-feedback/', views.admin_internal_feedback_list, name='admin_internal_feedback_list'),
    
    path('teacher/faq/', views.teacher_faq, name='teacher_faq'),
    path('teacher/playbook/', views.teacher_playbook, name='teacher_playbook'),
    path('teacher/rules/', views.teacher_rules, name='teacher_rules'),
    
    path('student/faq/', views.student_faq, name='student_faq'),
    path('student/rules/', views.student_rules, name='student_rules'),
    
    path('view-feedback/', views.view_feedback, name='view_feedback'),
]
