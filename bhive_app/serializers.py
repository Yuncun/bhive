from django.contrib.auth import get_user_model
from rest_framework import serializers

from bhive_app.models import Answer, Question


class EmbeddedAnswerSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(read_only=True)
    picture = serializers.ImageField(read_only=True)
    class Meta:
        model = Answer
        fields = ('id', 'picture', 'text', 'votes',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = EmbeddedAnswerSerializer(many=True, source='answer_set')

    class Meta:
        model = Question
        fields = ('id', 'answers', 'created_at', 'text', 'user_id',)


class AnswerSerializer(serializers.ModelSerializer):
    text = serializers.CharField(read_only=True)
    vote = serializers.BooleanField(required=True)
    picture = serializers.ImageField(read_only=True)
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'picture', 'text', 'votes',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'password',)

    def to_native(self, obj):
        """
        Remove password field when serializing an object
        """
        serialized = super(UserSerializer, self).to_native(obj)
        del serialized['password']
        return serialized
