import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from plates.models import Owner

client = Client()


class CreateOwnerTest(TestCase):
    def setUp(self):
        self.valid_owner = {
            'name': 'Nerijus',
            'surname': 'Stelionis'
        }

        self.invalid_owner = {
            'name': 'Nerijus',
            'surname': '--@@version'
        }

    def test_status_200(self):
        response = client.get(reverse('owners'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_owner(self):
        response = client.post(
            reverse('owners'),
            data=json.dumps(self.valid_owner),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_owner(self):
        response = client.post(
            reverse('owners'),
            data=json.dumps(self.invalid_owner),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CreatePlatesTest(TestCase):
    def setUp(self):
        owner = Owner.objects.create(name='Albert', surname='Einstein')

        self.valid_plate = {
            "license_number": "DEF911",
            "owner": owner.id
        }

        self.invalid_plate = {
            "license_number": "99DEE",
            "owner": owner.id
        }

        self.no_owner_plate = {
            "license_number": "GDP543",
        }

    def test_create_valid_plate(self):
        response = client.post(
            reverse('plates'),
            data=json.dumps(self.valid_plate),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_plate(self):
        response = client.post(
            reverse('plates'),
            data=json.dumps(self.invalid_plate),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_plate_without_owner(self):
        response = client.post(
            reverse('plates'),
            data=json.dumps(self.no_owner_plate),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_plate_two_times(self):
        response = client.post(
            reverse('plates'),
            data=json.dumps(self.valid_plate),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = client.post(
            reverse('plates'),
            data=json.dumps(self.valid_plate),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
