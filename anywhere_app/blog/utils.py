import os
import sys
import django
from django.utils import timezone
from datetime import timedelta

# Setup Django outside our main runtime
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'anywhere_app.settings')
django.setup()

from blog.models import Comment


def delete_comments():
    today = timezone.now()
    two_days = today - timedelta(days=2)

    query = Comment.objects.filter(updated_at__lte=two_days)
    query.delete()


def main():
    delete_comments()
main()
