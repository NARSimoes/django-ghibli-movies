
"""
    Core app models:
    - just the user models using allauth.
"""

import logging

from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in


logger = logging.getLogger(__name__)


def user_logged_in_receiver(request, user, **kwargs):
    logger.info(request, user)


# user model and connect
User = get_user_model()
user_logged_in.connect(user_logged_in_receiver, sender=User)
