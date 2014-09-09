from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView

from bhive_app.models import Answer, Question
from bhive_app.serializers import AnswerSerializer, QuestionSerializer


class QuestionsList(ListCreateAPIView):
    queryset = Question.objects.order_by('created_at')
    serializer_class = QuestionSerializer
    filter_fields = ('user_id',)


class QuestionsDetail(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerVote(UpdateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def pre_save(self, obj):
        vote = self.request.DATA.get('vote')
        if vote:
            obj.votes += 1