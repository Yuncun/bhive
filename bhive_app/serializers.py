from rest_framework import serializers

from bhive_app.models import Answer, Question


class EmbeddedAnswerSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'votes',)


class QuestionSerializer(serializers.ModelSerializer):
    answers = EmbeddedAnswerSerializer(many=True, source='answer_set')

    class Meta:
        model = Question
        fields = ('answers', 'created_at', 'text', 'user_id',)


class AnswerSerializer(serializers.ModelSerializer):
    text = serializers.CharField(read_only=True)
    vote = serializers.BooleanField(required=True)
    votes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Answer
        fields = ('id', 'text', 'votes',)