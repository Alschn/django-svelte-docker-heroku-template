from django.test import TestCase
from django.urls import reverse_lazy
from rest_framework import status


class ExampleViewTestCase(TestCase):
    url = reverse_lazy('example-view')

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'example/index.html')
        self.assertContains(response, 'Hello Django!')
