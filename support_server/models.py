# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    refresh_token = models.CharField(max_length=50)
    access_token = models.CharField(max_length=50)
    esp_code = models.CharField(max_length=8)
    strava_id = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'''{{
            id: {self.id}
            refresh_token: {self.refresh_token}
            access_token: {self.access_token}
            esp_code: {self.esp_code}
            strava_id: {self.strava_id}
        }}'''

