from django.db.models import (
    Model,
    CharField,
    TextField,
    BooleanField,
    DateTimeField
)


class Task(Model):
    title = CharField(max_length=255)
    description = TextField()
    completed = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
