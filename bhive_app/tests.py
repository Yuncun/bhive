import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from bhive_app.models import Answer, Question
from bhive_app.views import AnswerVote


class VotingViewTestCase(TestCase):
    factory = APIRequestFactory()

    def setUp(self):
        super(VotingViewTestCase, self).setUp()
        self.question = Question.objects.create(text='?', user_id='1')
        self.answer = self.question.answer_set.create(text='A')

    def test_data_missing(self):
        request = self.factory.put('/answers/1/', data={})
        view = AnswerVote.as_view()
        response = view(request, pk=self.answer.pk).render()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_put_false(self):
        request = self.factory.put('/answers/1/', data={'vote': False})
        view = AnswerVote.as_view()
        response = view(request, pk=self.answer.pk).render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        self.assertEqual(content['votes'], 0)
        answer = Answer.objects.get(pk=self.answer.pk)
        self.assertEqual(answer.votes, 0)

    def test_put(self):
        request = self.factory.put('/answers/1/', data={'vote': True})
        view = AnswerVote.as_view()
        response = view(request, pk=self.answer.pk).render()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)
        self.assertEqual(content['votes'], 1)
        answer = Answer.objects.get(pk=self.answer.pk)
        self.assertEqual(answer.votes, 1)