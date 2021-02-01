from django.test import TestCase
from django.urls import reverse_lazy

from ..models import BantamRank,FeatherRank


class TestBantamrankCreateView(TestCase):

    def test_create_bantamrank_success(self):
        params = {
            'user': '作成者','one': '1位','two': '2位','three': '3位','four': '4位',
            'five': '5位','six': '6位','seven': '7位','eight': '8位','nine': '9位','ten': '10位'
        }
        response = self.client.post(reverse_lazy('rizin_app:bantamrank_create'),params)

        self.assertRedirects(response,reverse_lazy('rizin_app:bantamrank_list'))

        self.assertEqual(BantamRank.objects.fillter(one='1位').count(),1)

    def test_create_bantamrank_failure(self):

        response = self.client.post(reverse_lazy('rizin_app:bantamrank_create'))

        self.assertFormError(response,'form','one','このフィールドは必須です。')


class TestFeatherrankCreateView(TestCase):

    def test_create_featherrank_success(self):
        params = {
            'user': '作成者', 'one': '1位', 'two': '2位', 'three': '3位', 'four': '4位',
            'five': '5位', 'six': '6位', 'seven': '7位', 'eight': '8位', 'nine': '9位', 'ten': '10位'
        }
        response = self.client.post(reverse_lazy('rizin_app:featherrank_create'), params)

        self.assertRedirects(response, reverse_lazy('rizin_app:featherrank_list'))

        self.assertEqual(FeatherRank.objects.fillter(one='1位').count(), 1)

    def test_create_featherrank_failure(self):
        response = self.client.post(reverse_lazy('rizin_app:featherrank_create'))

        self.assertFormError(response, 'form', 'one', 'このフィールドは必須です。')
