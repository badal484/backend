from mongoengine import Document, StringField

class Task(Document):
    title = StringField(required=True)
    description = StringField()
    completed = StringField(default="False")
