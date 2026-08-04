import os
import sys
import django
from pathlib import Path

# Force Django settings (fixes global Python issue)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Add project path to Python path for venv
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

django.setup()

from django.contrib.auth.models import User
from myapp.models import UserProfile, Property

print("Creating demo data in SQLite...")

# Demo Homeowner
user1, created = User.objects.get_or_create(
    username='demo_homeowner',
    defaults={'email': 'demo_homeowner@example.com'}
)
if created or not user1.check_password('demo123'):
    user1.set_password('demo123')
    user1.save()
UserProfile.objects.get_or_create(
    user=user1,
    defaults={'user_type': 'homeowner', 'phone': '9876543210'}
)
print(f"✅ Homeowner created: demo_homeowner / demo123")

# Demo Tenant
user2, created = User.objects.get_or_create(
    username='demo_tenant',
    defaults={'email': 'demo_tenant@example.com'}
)
if created or not user2.check_password('demo123'):
    user2.set_password('demo123')
    user2.save()
UserProfile.objects.get_or_create(
    user=user2,
    defaults={'user_type': 'user', 'phone': '9876543211'}
)
print(f"✅ Tenant created: demo_tenant / demo123")

# Demo Property 1
prop1 = Property.objects.get_or_create(
    title='Demo Single Room - Fergusson College Pune',
    owner=user1,
    defaults={
        'room_type': 'single',
        'flat_system': 'room',
        'city': 'Pune',
        'area_location': 'Fergusson College Road',
        'full_address': '123 Demo Society, Fergusson College Road, Pune 411004',
        'monthly_rent': 8500,
        'security_deposit': 17000,
        'maintenance_charges': 500,
        'max_people': 1,
        'floor_number': 2,
        'total_floors': 4,
        'furnishing_status': 'semi',
        'latitude': 18.5214,
        'longitude': 73.8499,
        'nearby_college_office': 'Fergusson College (0.3km), SP College (0.8km)',
        'preferred_tenant_type': 'students',
        'gender_preference': 'any',
        'available': True,
        'description': '✅ Demo single room for students. Semi-furnished with bed, wardrobe, study table. Perfect location near Fergusson College. 24/7 water, WiFi available.',
        'amenities': '["WiFi", "Parking", "24h Water", "Security", "Power Backup"]'
    }
)[0]
print(f"✅ Property 1 created: {prop1.title}")

print("\n🎉 Demo data successfully created!")
print("🔗 Visit http://127.0.0.1:8000/")
print("👤 Login as homeowner/tenant to test full flow")

