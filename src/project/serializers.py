from rest_framework import serializers
from .models import Project
from tag.models import Tag
from tag.serializers import TagSerializer


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, write_only=True, source="tags"
    )

    class Meta:
        model = Project
        fields = ["id", "title", "description", "tags", "tag_ids"]
