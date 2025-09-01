#!/usr/bin/env python
"""
Database initialization script for the educational platform
"""
import os
import sys
import django
from django.contrib.auth.models import User
from main.models import UserProfile, UniversityInfo


def init_database():
    """Initialize the database with sample data"""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    django.setup()

    print("Initializing database with sample data...")

    try:
        about_info, created = UniversityInfo.objects.get_or_create(
            page_type="about",
            defaults={
                "title": "О Московском Университете имени С.Ю. Витте",
                "content": """
                <h2>История университета</h2>
                <p>Московский Университет имени С.Ю. Витте – один из ведущих университетов России, 
                специализирующийся на экономическом образовании и подготовке высококвалифицированных 
                специалистов для различных отраслей экономики.</p>
                
                <p>Университет был основан в 1993 году и назван в честь Сергея Юльевича Витте – 
                выдающегося государственного деятеля России конца XIX – начала XX века, 
                министра финансов и председателя Совета министров Российской империи.</p>
                
                <h3>Наши достижения</h3>
                <ul>
                    <li>Более 15,000 студентов</li>
                    <li>500+ преподавателей</li>
                    <li>50+ образовательных программ</li>
                    <li>30 лет опыта в образовании</li>
                </ul>
                """,
                "is_active": True,
            },
        )
        if created:
            print("✓ Created about page information")
        else:
            print("✓ About page information already exists")

        contact_info, created = UniversityInfo.objects.get_or_create(
            page_type="contact",
            defaults={
                "title": "Контактная информация",
                "content": """
                <h2>Основные контакты</h2>
                <p><strong>Адрес:</strong> 115432, г. Москва, 2-й Кожуховский проезд, д. 12, стр. 1</p>
                <p><strong>Телефон:</strong> +7 (495) 123-45-67</p>
                <p><strong>Email:</strong> info@witte.ru</p>
                
                <h3>Режим работы</h3>
                <p>Пн-Пт: 9:00 - 18:00<br>
                Сб: 9:00 - 15:00<br>
                Вс: Выходной</p>
                
                <h3>Как добраться</h3>
                <p><strong>Метро:</strong> станция "Автозаводская" (Замоскворецкая линия)</p>
                <p><strong>Автобусы:</strong> № 8, 44, 142, 193, 703</p>
                """,
                "is_active": True,
            },
        )
        if created:
            print("✓ Created contact page information")
        else:
            print("✓ Contact page information already exists")

    except Exception as e:
        print(f"✗ Error creating university information: {e}")

    print("\nDatabase initialization completed!")


if __name__ == "__main__":
    init_database()
