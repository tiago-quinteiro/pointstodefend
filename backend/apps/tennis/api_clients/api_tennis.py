import requests
from django.conf import settings

BASE_URL = "https://api.api-tennis.com/tennis/"

def call_api(method, params=None):
    query = {
        "method": method,
        "APIkey": settings.API_TENNIS_KEY,
    }
    if params:
        query.update(params)

    response = requests.get(BASE_URL, params=query, timeout=10)
    response.raise_for_status()
    return response.json()
