from django.core.cache import cache
from faker import Faker
from rest_framework.test import APITestCase


class TestBase(APITestCase):
    fake = Faker()

    def tearDown(self):
        """
        Reset cache
        """

        cache.clear()

    @staticmethod
    def log_error(heading, url, payload, status, response):
        print(f'\n\n{heading}')
        print(f'URL: {url}')
        print(f'Payload: {payload}')
        print(f'Expected: {status}')
        print(f'Received: {response.status_code}')
        print(f'Response: {response.data}')
        print()

    def validate_delete(self, url, status):
        """
        Validate HTTP DELETE response
        """

        response = self.client.delete(url, format='json')

        if response.status_code != status:
            self.log_error('DELETE ERROR', url, None, status, response)

        self.assertEqual(response.status_code, status)
        return response

    def validate_get(self, url, status, query_params=None):
        """
        Validate HTTP GET response
        """

        response = self.client.get(url, query_params, format='json') if query_params else self.client.get(
            url,
            format='json'
        )

        if response.status_code != status:
            self.log_error('GET ERROR', url, None, status, response)

        self.assertEqual(response.status_code, status)
        return response

    def validate_patch(self, url, payload, status):
        """
        Validate HTTP PATCH response
        """

        response = self.client.patch(url, payload, format='json')

        if response.status_code != status:
            self.log_error('PATCH ERROR', url, payload, status, response)

        self.assertEqual(response.status_code, status)
        return response

    def validate_post(self, url, payload, status):
        """
        Validate HTTP POST response
        """

        response = self.client.post(url, payload, format='json')

        if response.status_code != status:
            self.log_error('POST ERROR', url, payload, status, response)

        self.assertEqual(response.status_code, status)
        return response
