
"""
    Core app views:
    - home_view: is the base!
"""

from django.shortcuts import render


def home_view(request, *args, **kwargs):
    """Home base view!"""
    return render(request, "base.html", {})
