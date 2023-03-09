from rest_framework import serializers
from rest_framework.decorators import permission_classes

from .models import BlogPost, BlogComment, BlogCategory


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BlogPost
        fields = '__all__'
        read_only_fields = ('author',)

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class BlogCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BlogComment
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        return BlogComment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance


class BlogCategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = BlogCategory
        fields = '__all__'
        read_only_fields = ('user',)

    def create(self, validated_data):
        return BlogCategory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
        return instance
