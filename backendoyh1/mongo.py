from mongoengine import connect
from django.conf import settings

def init_mongo():
    connect(host=settings.MONGO_URI)
