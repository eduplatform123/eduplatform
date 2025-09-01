from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.db import transaction
from .models import UserProfile, FeedbackForm, FeedbackAttachment, UniversityInfo, PublicFeedback, NewsArticle
from .forms import UserRegistrationForm, FeedbackFormForm, TeacherResponseForm, UserProfileForm, PublicFeedbackForm, NewsArticleForm
import os
import xlsxwriter
from io import BytesIO
from datetime import datetime

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.user_type == 'admin'

def is_teacher(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.user_type == 'teacher'

def is_student(user):
    return user.is_authenticated and hasattr(user, 'profile') and user.profile.user_type == 'student'

def logout_view(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы!')
    return redirect('home')

def home(request):
    return render(request, 'main/home.html')

def about_university(request):
    try:
        info = UniversityInfo.objects.get(page_type='about', is_active=True)
    except UniversityInfo.DoesNotExist:
        info = None
    return render(request, 'main/about.html', {'info': info})

def contact_info(request):
    try:
        info = UniversityInfo.objects.get(page_type='contact', is_active=True)
    except UniversityInfo.DoesNotExist:
        info = None
    return render(request, 'main/contact.html', {'info': info})

def faq(request):
    return render(request, 'main/faq.html')

def advantages(request):
    return render(request, 'main/advantages.html')

def programs(request):
    return render(request, 'main/programs.html')

def mission(request):
    return render(request, 'main/mission.html')

def public_feedback(request):
    if request.method == 'POST':
        form = PublicFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')
            return redirect('public_feedback')
    else:
        form = PublicFeedbackForm()
    
    return render(request, 'main/public_feedback.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    profile = UserProfile.objects.create(
                        user=user,
                        user_type='student',
                        student_id=form.cleaned_data['student_id'],
                    )
                    login(request, user)
                    messages.success(request, 'Регистрация прошла успешно!')
                    return redirect('dashboard')
            except Exception as e:
                messages.error(request, f'Ошибка при регистрации: {str(e)}')
                return render(request, 'main/register.html', {'form': form})
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'main/register.html', {'form': form})

@login_required
def dashboard(request):
    if not hasattr(request.user, 'profile'):
        if request.user.is_superuser:
            user_type = 'admin'
        else:
            user_type = 'student'
        
        UserProfile.objects.create(
            user=request.user,
            user_type=user_type
        )
        request.user.refresh_from_db()
    
    user_type = request.user.profile.user_type
    
    if user_type == 'admin':
        return redirect('admin_dashboard')
    
    if user_type == 'student':
        feedback_forms = FeedbackForm.objects.filter(student=request.user)
        pending_count = feedback_forms.filter(status='pending').count()
        completed_count = feedback_forms.filter(status='completed').count()
    elif user_type == 'teacher':
        feedback_forms = FeedbackForm.objects.filter(teacher=request.user)
        pending_count = feedback_forms.filter(status='pending').count()
        completed_count = feedback_forms.filter(status='completed').count()
    else:
        feedback_forms = FeedbackForm.objects.all()
        pending_count = feedback_forms.filter(status='pending').count()
        completed_count = feedback_forms.filter(status='completed').count()
        in_progress_count = feedback_forms.filter(status='in_progress').count()
    
    context = {
        'user_type': user_type,
        'feedback_forms': feedback_forms,
        'pending_count': pending_count,
        'completed_count': completed_count,
    }
    
    if user_type == 'admin':
        context['in_progress_count'] = in_progress_count
    
    return render(request, 'main/dashboard.html', context)

@login_required
def profile(request):
    if not hasattr(request.user, 'profile'):
        if request.user.is_superuser:
            user_type = 'admin'
        else:
            user_type = 'student'
        
        UserProfile.objects.create(
            user=request.user,
            user_type=user_type
        )
        request.user.refresh_from_db()
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлен!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)
    
    return render(request, 'main/profile.html', {'form': form})

@login_required
def create_feedback(request):
    if not is_student(request.user):
        messages.error(request, 'Только студенты могут создавать формы обратной связи.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FeedbackFormForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = request.user
            feedback.save()
            
            files = request.FILES.getlist('attachments')
            for file in files:
                FeedbackAttachment.objects.create(
                    feedback=feedback,
                    file=file,
                    filename=file.name
                )
            
            messages.success(request, 'Форма обратной связи отправлена!')
            return redirect('dashboard')
    else:
        form = FeedbackFormForm(user=request.user)
    
    return render(request, 'main/create_feedback.html', {'form': form})

@login_required
def feedback_form(request):
    if not is_student(request.user):
        messages.error(request, 'Только студенты могут создавать формы обратной связи.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FeedbackFormForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.student = request.user
            feedback.save()
            
            files = request.FILES.getlist('attachments')
            for file in files:
                FeedbackAttachment.objects.create(
                    feedback=feedback,
                    file=file,
                    filename=file.name
                )
            
            messages.success(request, 'Форма обратной связи отправлена!')
            return redirect('dashboard')
    else:
        form = FeedbackFormForm(user=request.user)
    
    return render(request, 'main/feedback_form.html', {'form': form})

@login_required
def feedback_detail(request, feedback_id):
    feedback = get_object_or_404(FeedbackForm, id=feedback_id)
    
    if not (request.user == feedback.student or 
            request.user == feedback.teacher or 
            is_admin(request.user)):
        messages.error(request, 'У вас нет прав для просмотра этой формы.')
        return redirect('dashboard')
    
    if request.method == 'POST' and (is_teacher(request.user) or is_admin(request.user)):
        form = TeacherResponseForm(request.POST, instance=feedback)
        if form.is_valid():
            feedback = form.save(commit=False)
            if form.cleaned_data['teacher_response']:
                feedback.response_date = timezone.now()
            feedback.save()
            messages.success(request, 'Ответ сохранен!')
            return redirect('feedback_detail', feedback_id=feedback.id)
    else:
        form = TeacherResponseForm(instance=feedback)
    
    context = {
        'feedback': feedback,
        'form': form,
        'can_respond': is_teacher(request.user) or is_admin(request.user)
    }
    
    return render(request, 'main/feedback_detail.html', context)

@login_required
def download_attachment(request, attachment_id):
    attachment = get_object_or_404(FeedbackAttachment, id=attachment_id)
    
    if not (request.user == attachment.feedback.student or 
            request.user == attachment.feedback.teacher or 
            is_admin(request.user)):
        messages.error(request, 'У вас нет прав для скачивания этого файла.')
        return redirect('dashboard')
    
    if os.path.exists(attachment.file.path):
        with open(attachment.file.path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{attachment.filename}"'
            return response
    else:
        raise Http404("Файл не найден")

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_students = UserProfile.objects.filter(user_type='student').count()
    total_teachers = UserProfile.objects.filter(user_type='teacher').count()
    total_feedback = FeedbackForm.objects.count()
    pending_feedback = FeedbackForm.objects.filter(status='pending').count()
    
    total_public_feedback = PublicFeedback.objects.count()
    new_public_feedback = PublicFeedback.objects.filter(status='new').count()
    
    recent_articles = NewsArticle.objects.all().order_by('-created_at')[:5]
    total_articles = NewsArticle.objects.count()
    published_articles = NewsArticle.objects.filter(status='published').count()
    
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_feedback': total_feedback,
        'pending_feedback': pending_feedback,
        'total_public_feedback': total_public_feedback,
        'new_public_feedback': new_public_feedback,
        'total_articles': total_articles,
        'published_articles': published_articles,
        'recent_articles': recent_articles,
    }
    
    return render(request, 'main/admin_dashboard.html', context)

@user_passes_test(is_admin)
def manage_users(request):
    if request.method == 'POST':
        if 'user_id' in request.POST and 'new_role' in request.POST:
            user_id = request.POST.get('user_id')
            new_role = request.POST.get('new_role')
            
            try:
                profile = UserProfile.objects.get(user_id=user_id)
                profile.user_type = new_role
                profile.save()
                messages.success(request, f'Роль пользователя {profile.user.username} изменена на {profile.get_user_type_display()}')
            except UserProfile.DoesNotExist:
                messages.error(request, 'Пользователь не найден')
        
        elif 'delete_user_id' in request.POST:
            user_id = request.POST.get('delete_user_id')
            try:
                user = User.objects.get(id=user_id)
                if not user.is_superuser:
                    username = user.username
                    user.delete()
                    messages.success(request, f'Пользователь {username} удален')
                else:
                    messages.error(request, 'Нельзя удалить суперпользователя')
            except User.DoesNotExist:
                messages.error(request, 'Пользователь не найден')
    
    search = request.GET.get('search', '')
    user_type = request.GET.get('user_type', '')
    
    users = UserProfile.objects.all().select_related('user')
    
    if search:
        users = users.filter(user__username__icontains=search)
    
    if user_type:
        users = users.filter(user_type=user_type)
    
    users = users.order_by('user__username')
    
    paginator = Paginator(users, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'main/manage_users.html', {'page_obj': page_obj})

@user_passes_test(is_admin)
def manage_university_info(request):
    if request.method == 'POST':
        pass
    
    info_pages = UniversityInfo.objects.all()
    return render(request, 'main/manage_university_info.html', {'info_pages': info_pages})

@user_passes_test(is_admin)
def mark_public_feedback_worked(request, feedback_id):
    if request.method == 'POST':
        try:
            feedback = PublicFeedback.objects.get(id=feedback_id)
            feedback.status = 'completed'
            feedback.save()
            messages.success(request, f'Обращение от {feedback.name} отмечено как обработанное')
        except PublicFeedback.DoesNotExist:
            messages.error(request, 'Обращение не найдено')
    
    return redirect('admin_dashboard')

@user_passes_test(is_admin)
def public_feedback_detail(request, feedback_id):
    try:
        feedback = PublicFeedback.objects.get(id=feedback_id)
    except PublicFeedback.DoesNotExist:
        messages.error(request, 'Обращение не найдено.')
        return redirect('admin_dashboard')
    
    return render(request, 'main/public_feedback_detail.html', {'feedback': feedback})

@user_passes_test(is_admin)
def download_teacher_statistics(request):
    output = BytesIO()
    
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet('Статистика преподавателей')
    
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    cell_format = workbook.add_format({
        'text_wrap': True,
        'valign': 'top',
        'border': 1
    })
    
    worksheet.set_column('A:A', 25)
    worksheet.set_column('B:B', 15)
    worksheet.set_column('C:C', 12)
    worksheet.set_column('D:D', 12)
    worksheet.set_column('E:E', 12)
    worksheet.set_column('F:F', 12)
    worksheet.set_column('G:G', 12)
    
    headers = [
        'Преподаватель',
        'Email',
        'Всего обращений',
        'Ожидающих',
        'В работе',
        'Завершено',
        'Отклонено'
    ]
    
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)
    
    teachers = UserProfile.objects.filter(user_type='teacher').select_related('user')
    
    row = 1
    for teacher_profile in teachers:
        teacher = teacher_profile.user
        
        feedback_stats = FeedbackForm.objects.filter(teacher=teacher).aggregate(
            total=Count('id'),
            pending=Count('id', filter=Q(status='pending')),
            in_progress=Count('id', filter=Q(status='in_progress')),
            completed=Count('id', filter=Q(status='completed')),
            rejected=Count('id', filter=Q(status='rejected'))
        )
        
        worksheet.write(row, 0, teacher.get_full_name() or teacher.username, cell_format)
        worksheet.write(row, 1, teacher.email, cell_format)
        worksheet.write(row, 2, feedback_stats['total'], cell_format)
        worksheet.write(row, 3, feedback_stats['pending'], cell_format)
        worksheet.write(row, 4, feedback_stats['in_progress'], cell_format)
        worksheet.write(row, 5, feedback_stats['completed'], cell_format)
        worksheet.write(row, 6, feedback_stats['rejected'], cell_format)
        
        row += 1
    
    if teachers.exists():
        worksheet.write(row, 0, 'ИТОГО:', header_format)
        worksheet.write(row, 1, '', header_format)
        
        total_feedback = FeedbackForm.objects.count()
        total_pending = FeedbackForm.objects.filter(status='pending').count()
        total_in_progress = FeedbackForm.objects.filter(status='in_progress').count()
        total_completed = FeedbackForm.objects.filter(status='completed').count()
        total_rejected = FeedbackForm.objects.filter(status='rejected').count()
        
        worksheet.write(row, 2, total_feedback, header_format)
        worksheet.write(row, 3, total_pending, header_format)
        worksheet.write(row, 4, total_in_progress, header_format)
        worksheet.write(row, 5, total_completed, header_format)
        worksheet.write(row, 6, total_rejected, header_format)
    
    workbook.close()
    
    output.seek(0)
    filename = f'teacher_statistics_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
    
    response = HttpResponse(
        output.read(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


def news_list(request):
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    
    articles = NewsArticle.objects.filter(status='published')
    
    if category:
        articles = articles.filter(category=category)
    
    if search:
        articles = articles.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search) |
            Q(excerpt__icontains=search) |
            Q(tags__icontains=search)
        )
    
    featured_articles = articles.filter(is_featured=True)[:3]
    
    recent_articles = articles[:10]
    
    categories = NewsArticle.objects.filter(status='published').values_list('category', flat=True).distinct()
    
    context = {
        'featured_articles': featured_articles,
        'recent_articles': recent_articles,
        'categories': categories,
        'current_category': category,
        'search_query': search,
    }
    
    return render(request, 'main/news_list.html', context)


def news_detail(request, slug):
    try:
        article = NewsArticle.objects.get(slug=slug, status='published')
        article.views_count += 1
        article.save(update_fields=['views_count'])
    except NewsArticle.DoesNotExist:
        messages.error(request, 'Статья не найдена.')
        return redirect('news_list')
    
    related_articles = NewsArticle.objects.filter(
        status='published',
        category=article.category
    ).exclude(id=article.id)[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    
    return render(request, 'main/news_detail.html', context)


@user_passes_test(is_admin)
def create_news_article(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, f'Статья "{article.title}" успешно создана!')
            return redirect('admin_dashboard')
    else:
        form = NewsArticleForm()
    
    context = {
        'form': form,
        'is_creating': True,
    }
    
    return render(request, 'main/create_news_article.html', context)


@user_passes_test(is_admin)
def edit_news_article(request, article_id):
    try:
        article = NewsArticle.objects.get(id=article_id)
    except NewsArticle.DoesNotExist:
        messages.error(request, 'Статья не найдена.')
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, f'Статья "{article.title}" успешно обновлена!')
            return redirect('admin_dashboard')
    else:
        form = NewsArticleForm(instance=article)
    
    context = {
        'form': form,
        'article': article,
        'is_creating': False,
    }
    
    return render(request, 'main/create_news_article.html', context)

@user_passes_test(is_admin)
def admin_public_feedback_list(request):
    public_feedback_forms = PublicFeedback.objects.all().order_by('-created_at')
    
    context = {
        'public_feedback_forms': public_feedback_forms,
    }
    
    return render(request, 'main/admin_public_feedback_list.html', context)


@user_passes_test(is_admin)
def admin_internal_feedback_list(request):
    feedback_forms = FeedbackForm.objects.all().order_by('-created_at')
    
    context = {
        'feedback_forms': feedback_forms,
    }
    
    return render(request, 'main/admin_internal_feedback_list.html', context)


@user_passes_test(is_teacher)
def teacher_faq(request):
    return render(request, 'main/teacher_faq.html')


@user_passes_test(is_teacher)
def teacher_playbook(request):
    return render(request, 'main/teacher_playbook.html')


@user_passes_test(is_teacher)
def teacher_rules(request):
    return render(request, 'main/teacher_rules.html')


@user_passes_test(is_student)
def student_faq(request):
    return render(request, 'main/student_faq.html')


@user_passes_test(is_student)
def student_rules(request):
    return render(request, 'main/student_rules.html')


@login_required
def view_feedback(request):
    user_type = request.user.profile.user_type
    
    if user_type == 'student':
        feedback_forms = FeedbackForm.objects.filter(student=request.user)
    elif user_type == 'teacher':
        feedback_forms = FeedbackForm.objects.filter(teacher=request.user)
    elif user_type == 'admin':
        feedback_forms = FeedbackForm.objects.all()
    else:
        feedback_forms = []
    
    context = {
        'feedback_forms': feedback_forms,
        'user_type': user_type,
    }
    
    return render(request, 'main/view_feedback.html', context)
