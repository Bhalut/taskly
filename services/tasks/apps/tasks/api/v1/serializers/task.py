from rest_framework.serializers import (
    Serializer,
    CharField,
    IntegerField,
    BooleanField,
    DateTimeField,
)


class TaskCreateSerializer(Serializer):
    title = CharField(max_length=255)
    description = CharField()


class TaskUpdateSerializer(Serializer):
    title = CharField(max_length=255)
    description = CharField()
    completed = BooleanField()


class TaskSerializer(Serializer):
    id = IntegerField()
    title = CharField(max_length=255)
    description = CharField()
    completed = BooleanField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
