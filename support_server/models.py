# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    refresh_token = models.CharField(max_length=50)
    access_token = models.CharField(max_length=50)
    esp_code = models.CharField(max_length=50)

