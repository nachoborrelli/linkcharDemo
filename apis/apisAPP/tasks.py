from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery.utils.log import get_task_logger
from .models import Entry
import requests
import json

logger = get_task_logger(__name__)


def get_data(url):
        response_API = requests.get(url)
        data = response_API.text
        return json.loads(data)


def save_data():
        data = get_data("https://api.publicapis.org/entries")
        for entry in data["entries"]:
            a_entry_creation.delay(entry)

        return "Celery has load everything"

@shared_task(bind=True, track_started=True)
def a_entry_creation(self, entry):
    Entry.objects.create(
                api=entry['API'],
                description = entry['Description'],
                auth = entry['Auth'],
                https = entry['HTTPS'],
                cors = entry['Cors'],
                link = entry['Link'],
                category = entry['Category']
                )

    