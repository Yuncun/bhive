from django.db.models import F
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.response import Response

from bhive_app.models import Answer, Question
from bhive_app.serializers import AnswerSerializer, QuestionSerializer


TRUE_VALUES = ['True', 'true', 1]


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

    def update(self, request, *args, **kwargs):
        vote = self.request.DATA.get('vote', None)
        obj = self.get_object_or_none()

        if vote is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if vote in TRUE_VALUES:
            Answer.objects.filter(id__in=[obj.pk]).update(votes=F('votes') + 1)

        obj = self.get_object_or_none()
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)