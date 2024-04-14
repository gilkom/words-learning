# create_tokens.py

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'words_learning.settings')

import django
django.setup()

from nauka.models import User  # Zmieniona nazwa klasy User
from rest_framework.authtoken.models import Token

def create_tokens():
    users = User.objects.all()

    for user in users:
        Token.objects.get_or_create(user=user)

if __name__ == '__main__':
    create_tokens()