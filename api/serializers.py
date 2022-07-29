from .models import Idea, Saves
from rest_framework import serializers
from django.contrib.auth.models import User

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Idea
        fields = '__all__'

        def create(self, data):
            return Idea.objects.create(data)

        def update(self, instance, data):
            instance.name = data.get('name', instance.name)
            instance.likes = data.get('likes', instance.likes)
            instance.dislikes = data.get('dislikes', instance.dislikes)
            instance.save()
            return instance

class SaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Saves
        fields = '__all__'

        def create(self, data):
            return Saves.objects.create(data)

        def update(self, instance, data):
            instance.user = data.get('user', User)
            instance.image = data.get('image', instance.image)

